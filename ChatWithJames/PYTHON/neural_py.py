"""Rete neurale TensorFlow con tre matrici di pesi."""

import tensorflow as tf


class ReteNeurale(tf.keras.Model):
	"""Perceptron multistrato: input -> hidden1 -> hidden2 -> output."""

	def __init__(self, dimensione_input, neuroni_1, neuroni_2, dimensione_output):
		super().__init__()
		self.W1 = self.add_weight(
			name="W1", shape=(dimensione_input, neuroni_1),
			initializer="glorot_uniform", trainable=True
		)
		self.W2 = self.add_weight(
			name="W2", shape=(neuroni_1, neuroni_2),
			initializer="glorot_uniform", trainable=True
		)
		self.W3 = self.add_weight(
			name="W3", shape=(neuroni_2, dimensione_output),
			initializer="glorot_uniform", trainable=True
		)

	def call(self, inputs):
		"""Restituisce una matrice di output per l'intero batch."""
		inputs = tf.cast(inputs, tf.float32)
		hidden_1 = tf.nn.relu(tf.matmul(inputs, self.W1))
		hidden_2 = tf.nn.relu(tf.matmul(hidden_1, self.W2))
		return tf.matmul(hidden_2, self.W3)


if __name__ == "__main__":
	modello = ReteNeurale(4, 8, 4, 2)
	esempio = tf.random.normal((3, 4))
	print("Output:", modello(esempio).numpy())
