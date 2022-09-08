import tensorflow as tf
from keras.layers import Dense, Activation, Dropout

class ChatBotModel(tf.keras.Model):

    def __init__(self, input_shape, output_shape):
        super().__init__()
        self.dense1 = Dense(128,input_shape= input_shape, activation='relu')
        self.dropout1 = Dropout(0.5)
        self.dense2 = Dense(64, activation='relu')
        self.dropout2 = Dropout(0.5)
        self.dense3 = Dense(output_shape, activation='softmax')

    def call(self, inputs):
        z1 = self.dense1(inputs)
        y1 = self.dropout1(z1)

        z2 = self.dense2(y1)
        y2 = self.dropout2(z2)

        return self.dense3(y2)

    def get_config(self):
        base_config = super().get_config()
        return {**base_config}