from torchtext import data
from torchtext import datasets


# Approach 1:
# set up fields
TEXT = data.Field()
LABEL = data.Field(sequential=False)

# make splits for data
train, val, test = datasets.SST.splits(
    TEXT, LABEL, fine_grained=True, train_subtrees=True,
    filter_pred=lambda ex: ex.label != 'neutral')

# print information about the data
print('train.fields', train.fields)
print('len(train)', len(train))
print('vars(train[0])', vars(train[0]))

# build the vocabulary

TEXT.build_vocab(train, vectors='glove.6B.300d')
LABEL.build_vocab(train)

# print vocab information
print('len(TEXT.vocab)', len(TEXT.vocab))
print('TEXT.vocab.vectors.size()', TEXT.vocab.vectors.size())

# make iterator for splits
train_iter, val_iter, test_iter = data.BucketIterator.splits(
    (train, val, test), batch_size=3, device=0)

# print batch information
batch = next(iter(train_iter))
print(batch.text)
print(batch.label)

# Approach 2:
TEXT.build_vocab(train, vectors=['glove.840B.300d', 'charngram.100d'])
LABEL.build_vocab(train)

# print vocab information
print('len(TEXT.vocab)', len(TEXT.vocab))
print('TEXT.vocab.vectors.size()', TEXT.vocab.vectors.size())


train_iter, val_iter, test_iter = datasets.SST.iters(batch_size=4)

# print batch information
batch = next(iter(train_iter))
print(batch.text)
print(batch.label)
