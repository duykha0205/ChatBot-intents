import imp
import os
import sys
import pickle as pkl
import logging
import argparse
import random
from model import ChatBotModel
from tensorflow.keras.optimizers import SGD
from gui import *
from tkinter import *
from app import appWeb


def main():
    parser = argparse.ArgumentParser('Tensorflow')
    parser.add_argument('--mode', default='app',
                        help='mode fold you will try.')

    args = parser.parse_args()

    if args.mode == 'train':
        from train_chatbot import model
        print("----TRAIN MODE------")
        model.save('chatbot_model.h5py')
        print("model created")

    elif args.mode == 'app':
        print("----APP MODE------")
        root=Tk()
        app = ChatInterface(root)
        window_size="400x400"
        root.geometry(window_size)
        root.title("Elon- General Chatbot")
        #root.iconbitmap('i.ico')
        root.mainloop()

    elif args.mode == 'web':
        print("----WEB MODE------")
        appWeb.run(debug=True)

   
    print("------DONE!-----")


def train(network, data_generator, keep_prob, epochs, data_name,
          mode='train_0', batch_size=20, nb_classes=2, shuffle=True,
          is_val=True, is_test=True, save_best=True, ways='crf'):
    
    model = ChatBotModel(input_shape=(len(train_x[0]),), output_shape=len(train_y[0]))


    # # Compile model. Stochastic gradient descent with Nesterov accelerated gradient gives good results for this model
    # sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
    # model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

    # #fitting and saving the model 
    # hist = model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)
    # model.save('chatbot_model.h5py')
    # print("model created")



if __name__ == '__main__':
    main()