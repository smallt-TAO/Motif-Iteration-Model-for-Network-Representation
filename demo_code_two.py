# !/usr/bin/env python

"""
__author__ = 'Smalltao'

"""

from __future__ import print_function
import scale_free_ba
import ncn_small_word
import random_network_er
import ncn_word
from algorithm import matrix_random
from algorithm import matrix_change

import time
import numpy as np

import theano
import theano.tensor as T
import lasagne


def load_data_matrix(size=400, n=50):
    y_label = np.array([0 for i in range(size)])
    x_image = np.zeros((size, 1, n, n))
    echo = int(size / 200)
    iter_num = 0
    print("start to make matrix>>>>>>")
    print("small_word>>>>>>>>>")
    for k in [5, 8, 11, 14, 15]:
        for p in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.6, 0.7, 0.75, 0.8]:
            for ii in range(echo):
                ws = ncn_small_word.small_word(n, k, p)
                ws = matrix_random(ws)
                ws = matrix_change(ws)
                y_label[iter_num] = 1
                x_image[iter_num, :, :, :] = ws
                iter_num += 1
    print("iter_num = " + str(iter_num))

    print("normal network>>>>>>>>>>")
    for num in [3, 4, 5, 6, 7]:
        for si in range(10):
            for ii in range(echo):
                nn = ncn_word.normal_word(n, num)
                nn = matrix_random(nn)
                nn = matrix_change(nn)
                y_label[iter_num] = 0
                x_image[iter_num, :, :, :] = nn
                iter_num += 1
    print("iter_num = " + str(iter_num))

    print("scale free network>>>>>>>>>")
    for num in [2, 3, 4, 5, 6]:
        for m in [2, 3, 5, 6, 7, 8, 9, 10, 11, 12]:
            for ii in range(echo):
                ba = scale_free_ba.scale_free(n, num, m)
                ba = matrix_random(ba)
                ba = matrix_change(ba)
                y_label[iter_num] = 3
                x_image[iter_num, :, :, :] = ba
                iter_num += 1
    print("iter_num = " + str(iter_num))

    print("random network>>>>>>>>>")
    for p in [0.10, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.20]:
        for si in range(5):
            for ii in range(echo):
                er = random_network_er.random_network(n, p)
                er = matrix_random(er)
                er = matrix_change(er)
                y_label[iter_num] = 2
                x_image[iter_num, :, :, :] = er
                iter_num += 1
    print("iter_num = " + str(iter_num))

    y_label = y_label.reshape((size,))
    x_image = x_image.reshape((size, 1, n, n))

    return x_image, y_label


def load_text_data(size=5, n=50):
    x_image = np.zeros((size, 1, n, n))
    num = 50
    matrix_data = [([0] * num) for si in range(num)]
    for i in range(5):
        fr = open("test_data\\{0}.txt".format(i))
        for eachLine in fr:
            line = eachLine.strip().split()
            for j in range(1, len(line)):
                (m, n) = (int(line[0]) - 1, int(line[j]) - 1)
                matrix_data[m][n] = 1
                matrix_data[n][m] = 1
            x_image[i, :, :, :] = matrix_data

    return x_image


def build_cnn(input_var=None):
    network = lasagne.layers.InputLayer(shape=(None, 1, 50, 50), input_var=input_var)

    network = lasagne.layers.Conv2DLayer(
            network, num_filters=32, filter_size=(5, 5),
            nonlinearity=lasagne.nonlinearities.rectify,
            W=lasagne.init.GlorotUniform())

    network = lasagne.layers.MaxPool2DLayer(network, pool_size=(2, 2))

    network = lasagne.layers.Conv2DLayer(
            network, num_filters=32, filter_size=(5, 5),
            nonlinearity=lasagne.nonlinearities.rectify)
    network = lasagne.layers.MaxPool2DLayer(network, pool_size=(2, 2))

    network = lasagne.layers.DenseLayer(
            lasagne.layers.dropout(network, p=.5),
            num_units=256,
            nonlinearity=lasagne.nonlinearities.rectify)

    network = lasagne.layers.DenseLayer(
            lasagne.layers.dropout(network, p=.5),
            num_units=4,
            nonlinearity=lasagne.nonlinearities.softmax)

    return network


def iterate_mini_batches(inputs, targets, batch_size, shuffle=False):
    assert len(inputs) == len(targets)
    if shuffle:
        indices = np.arange(len(inputs))
        np.random.shuffle(indices)
    for start_idx in range(0, len(inputs) - batch_size + 1, batch_size):
        if shuffle:
            excerpt = indices[start_idx:start_idx + batch_size]
        else:
            excerpt = slice(start_idx, start_idx + batch_size)
        yield inputs[excerpt], targets[excerpt]


def main(model='cnn', num_epochs=10):
    print("Loading data...")
    X_train, y_train = load_data_matrix(4000)
    X_val, y_val = load_data_matrix(800)
    X_test, y_test = load_data_matrix(800)
    X_test1 = load_text_data(5)

    input_var = T.tensor4('inputs')
    target_var = T.ivector('targets')

    if model == 'cnn':
        network = build_cnn(input_var)
    else:
        print("Unrecognized model type %r." % model)
        return

    prediction = lasagne.layers.get_output(network)
    loss = lasagne.objectives.categorical_crossentropy(prediction, target_var)
    loss = loss.mean()

    params = lasagne.layers.get_all_params(network, trainable=True)
    updates = lasagne.updates.nesterov_momentum(loss, params, learning_rate=0.01, momentum=0.9)

    test_prediction = lasagne.layers.get_output(network, deterministic=True)
    test_loss = lasagne.objectives.categorical_crossentropy(test_prediction, target_var)

    # This agr for the prediction data.
    prediction = T.argmax(test_prediction, axis=1)
    test_loss = test_loss.mean()
    test_acc = T.mean(T.eq(prediction, target_var), dtype=theano.config.floatX)

    train_fn = theano.function([input_var, target_var], loss, updates=updates, allow_input_downcast=True)
    val_fn = theano.function([input_var, target_var], [test_loss, test_acc], allow_input_downcast=True)
    prediction_fn = theano.function(
        input_var, prediction, allow_input_downcast=True, on_unused_input='warn')

    print("Starting training...")
    for epoch in range(num_epochs):
        # In each epoch, we do a full pass over the training data:
        train_err = 0
        train_batches = 0
        start_time = time.time()
        for batch in iterate_mini_batches(X_train, y_train, 50, shuffle=True):
            inputs, targets = batch
            train_err += train_fn(inputs, targets)
            train_batches += 1

        # And a full pass over the validation data:
        val_err = 0
        val_acc = 0
        val_batches = 0
        for batch in iterate_mini_batches(X_val, y_val, 50, shuffle=False):
            inputs, targets = batch
            err, acc = val_fn(inputs, targets)
            val_err += err
            val_acc += acc
            val_batches += 1

        # Then we print the results for this epoch:
        print("Epoch {} of {} took {:.3f}s".format(epoch + 1, num_epochs, time.time() - start_time))
        print("  training loss:\t\t{:.6f}".format(train_err / train_batches))
        print("  validation loss:\t\t{:.6f}".format(val_err / (val_batches + 0.000001)))
        print("  validation accuracy:\t\t{:.2f} %".format(val_acc / (val_batches + 0.0000001) * 100))

    # After training, we compute and print the test error:
    test_err = 0
    test_acc = 0
    test_batches = 0
    for batch in iterate_mini_batches(X_test, y_test, 50, shuffle=False):
        inputs, targets = batch
        err, acc = val_fn(inputs, targets)
        test_err += err
        test_acc += acc
        test_batches += 1
        print(prediction_fn(inputs))
    print("Final results:")
    print("  test loss:\t\t\t{:.6f}".format(test_err / test_batches))
    print("  test accuracy:\t\t{:.2f} %".format(test_acc / test_batches * 100))

    # third community find vision.
    print(prediction_fn(X_test1))


if __name__ == '__main__':
    main()
