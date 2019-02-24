import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# LOAD DATASET
mnist = input_data.read_data_sets("../datasets/MNIST_data/", one_hot=True)

# CONFIG
image_size = 28 # Size of the input image data - length of one side
labels_size = 10 # Size of the Set<PossibleLabels>
learning_rate = 0.05 # Size of incremental calibrations made to weights/biases
steps_number = 10000 # Num of iterations of optimization
batch_size = 100 # Num of input images to be trained on, at a time.

# DEFINE COMPUTATIONAL GRAPH

# Define placeholders
training_data = tf.placeholder(tf.float32, [None, image_size*image_size])
labels = tf.placeholder(tf.float32, [None, labels_size])

# Variables to be tuned
W = tf.Variable(tf.truncated_normal([image_size*image_size, labels_size], stddev=0.1))
b = tf.Variable(tf.constant(0.1, shape=[labels_size]))

# Build the network (only output layer)
output = tf.matmul(training_data, W) + b

# Optimize (minimize) the loss function (loss = predictions - actual label values)
# Use "Cross entropy" technique of Neural Nets to define the losses
# X-entropy internally applies softmax on the model's unnormalized prediction and sums across all classes
softmax_cross_entropy = tf.nn.softmax_cross_entropy_with_logits(labels=labels, logits=output)

# Define the loss function
loss = tf.reduce_mean(softmax_cross_entropy)

# Training step - utilize the Gradient Descent algorithm
# The GradientDescent Optimizer will adjust the values of W and b to minimize loss.
train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss)

# Evaluate the accuracy of predictions
correct_prediction = tf.equal(tf.argmax(output, 1), tf.argmax(labels, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))


# TRAINING

# Run the training
sess = tf.InteractiveSession()
sess.run(tf.global_variables_initializer())

for i in range(steps_number):
  # Load the next batch
  input_batch, labels_batch = mnist.train.next_batch(batch_size)
  feed_dict = {
    training_data: input_batch,
    labels: labels_batch
  }

  # Run the training step
  train_step.run(feed_dict=feed_dict)

  # Evaluation status on the batch (1 every 100 steps)
  if i % 1000 == 0:
    train_accuracy = accuracy.eval(feed_dict=feed_dict)
    print("STEP %d, training batch accuracy %g %%" % (i, train_accuracy * 100))



# APPLY THE MODEL

# Evaluate model's prediction accuracy against new test data
test_dict = {
  training_data: mnist.test.images,
  labels: mnist.test.labels
}
test_accuracy = accuracy.eval(feed_dict=test_dict)
print("Test accuracy: %g %%" % (test_accuracy * 100))