import splitfolders

splitfolders.ratio("data", output="data_final",
    seed=1337, ratio=(.6, .2, .2), group_prefix=None, move=False)