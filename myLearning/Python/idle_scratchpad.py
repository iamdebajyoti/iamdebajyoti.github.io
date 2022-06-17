_selection_ = input()
_selection_ = _selection_.replace(" ",",")
_selection_ = _selection_.replace(";",",")
_selection_ = _selection_.replace(",,",",")
while (_selection_.count(",,",1) >=1):
    _selection_ = _selection_.replace(",,",",")
print(_selection_, type(_selection_))
_selection_ = _selection_.split(sep=",")
print(_selection_, type(_selection_))
for _i_ in range(len(_selection_)-1):
    print(_selection_[_i_], type(_selection_[_i_]))
    if _selection_[_i_] == '':
        _selection_.pop(_i_)
print(_selection_)
for _f_ in _selection_:
    print(_f_, type(_f_))
    print(int(_f_), type(int(_f_)))
