import pytest
from fastai import *
from fastai.vision import *
from fastai.widgets import *

np.random.seed(42)

@pytest.fixture(scope="module")
def data():
    path = untar_data(URLs.MNIST_TINY)
    data = ImageDataBunch.from_folder(path, ds_tfms=(rand_pad(2, 28), []), batch_size=16, num_workers=2)
    return data

def test_image_cleaner_index_length_too_long(data):
    with pytest.raises(AssertionError) as e:
        n = len(data.valid_ds)
        assert  ImageCleaner(data.valid_ds, np.arange(n+1))
                   
def test_image_cleaner_index_length_too_short(data):
    with pytest.raises(AssertionError) as e:    
        n = len(data.valid_ds)
        assert ImageCleaner(data.valid_ds, np.arange(n+1))
        
def test_image_cleaner_length_correct(data):
    with pytest.raises(AssertionError) as e:
        n = len(data.valid_ds)
        ImageCleaner(data.valid_ds, np.arange(n))
        
@pytest.mark.xfail(reason = "Expected Fail")                   
def test_image_cleaner_wrong_input_type(data):
    n = len(data.valid_ds)
    ImageCleaner(data, np.arange(n))
    

    
 
