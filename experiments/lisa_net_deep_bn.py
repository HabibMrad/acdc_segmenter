import model_zoo
import tensorflow as tf

experiment_name = 'lisa_net_deep_bn'

batch_size = 10
learning_rate = 0.01
data_file = 'data_288x288.hdf5'
model_handle = model_zoo.lisa_net_deeper_bn
optimizer_handle = tf.train.AdamOptimizer

schedule_lr = False
warmup_training = True
augment_batch = True
weight_decay = 0.00000
momentum = None