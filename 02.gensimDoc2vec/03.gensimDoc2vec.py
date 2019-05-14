from gensim.models import doc2vec
import sys
import multiprocessing

# reload(sys)
# sys.setdefaultencoding('utf-8')

cores = multiprocessing.cpu_count()

#doc2vec parameters
vector_size = 300
window_size = 15
word_min_count = 2
sampling_threshold = 1e-5
negative_size = 5
train_epoch = 100
dm = 1 # 0= dbow; 1 =dmpv