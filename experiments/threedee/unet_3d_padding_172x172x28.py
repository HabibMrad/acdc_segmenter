import model_zoo3d
import tensorflow as tf

experiment_name = 'unet_3D_padding_172x172x28'

batch_size = 1
learning_rate = 0.01
data_file = 'data3D_172x172x28.hdf5'
image_size = (172,172,28)
model_handle = model_zoo3d.unet3D_bn_padded
optimizer_handle = tf.train.AdamOptimizer
input_dataset = 'images'
input_channels = 1
down_sampling_factor = 1  # 1 means no down samplign, 2 means half the size (must be int)

schedule_lr = False
warmup_training = True
weight_decay = 0.00000
momentum = None
loss_type = 'weighted_crossentropy'  # crossentropy/weighted_crossentropy/dice

# Augmentation settings
augment_batch = False
do_rotations = True
do_scaleaug = False
do_fliplr = False

# Rarely used settings
use_data_fraction = False  # Should normally be False