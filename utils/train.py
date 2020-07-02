import fasttext

# 打印评价结果
def print_results(N, p, r):
    print("N\t" + str(N))
    print("P@{}\t{:.3f}".format(1, p))
    print("R@{}\t{:.3f}".format(1, r))


model = fasttext.train_supervised("train_all.txt", dim=60, epoch=50, lr=0.1, loss="hs")

#预测 打印5个结果
print(model.predict("我",k=5)

# 压缩
model.quantize(input="train_all.txt", qnorm=True, retrain=True, cutoff=100000)

print_results(*model.test("test.txt"))

model.save_model("model.ftz")
