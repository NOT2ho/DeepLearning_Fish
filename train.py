import sys
sys.path.append('..') 
from trainer import Trainer
from optimizer import Adam
from simpleCBOW import SimpleCBOW
from preprocess import preprocess
from create_contexts_target import create_contexts_target
from convert_one_hot import convert_one_hot
 

window_size = 1
hidden_size = 5
batch_size = 3
max_epoch = 1000

text = 'poor simuruk cat is very very poor and mimi'
corpus, word_to_id, id_to_word = preprocess(text)

vocab_size = len(word_to_id)
contexts, target = create_contexts_target(corpus, window_size)
target = convert_one_hot(target, vocab_size)
contexts = convert_one_hot(contexts, vocab_size)

model = SimpleCBOW(vocab_size, hidden_size)
optimizer = Adam()
trainer = Trainer(model, optimizer)

trainer.fit(contexts, target, max_epoch, batch_size)
trainer.plot()

word_vecs = model.word_vecs
for word_id, word in id_to_word.items():
    print(word, word_vecs[word_id])