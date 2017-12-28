Origin from https://github.com/junxiaosong/AlphaZero_Gomoku
## AlphaZero-Gomoku
本專案用來實作 AlphaGo-Zero 演算法來玩五子棋(Gobang or Gomoku)
需要訓練產生 model 檔，一般 PC 可能需要數小時

參考文件：
1. AlphaZero: Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm
2. AlphaGo Zero: Mastering the game of Go without human knowledge

### 範例: Games Between Trained Models
- Each move  with 400 playouts:  
![playout400](https://raw.githubusercontent.com/junxiaosong/AlphaZero_Gomoku/master/playout400.gif)
- Each move  with 800 playouts:  
![playout800](https://raw.githubusercontent.com/junxiaosong/AlphaZero_Gomoku/master/playout800.gif)

### 系統需求:
要使用本專案玩五子棋，系統需要底下套件
- Python >= 3.0 (通常ubuntu 都內建)
- Numpy >= 1.11 (sudo pip3 install numpy)

要訓練 AI model，需要底下兩個套件:
- Theano == 0.7 (目前僅能使用此版本, sudo pip3 install theano==0.7.0)
- Lasagne >= 0.1 (sudo pip3 install lasagne)

**PS**:
  1) theano 有新版，但是會出錯，可以參考 [issue](https://github.com/aigamedev/scikit-neuralnetwork/issues/235)
     也就是說，新版的 theano, 用下面的命令安裝開發版本的 Lasagne:
     pip3 install --upgrade https://github.com/Lasagne/Lasagne/archive/master.zip
     pip3 install --upgrade theano
  2) 如果你想要用別種 DL frameworks 來產生 model, 像 TensorFlow or PyTorch, 只需要重寫 policy_value_net.py 即可

### 開始:
要玩現有 model 的五子棋:
> python3 human_play.py  
或
> chmod a+x human_play.py
> ./human_play.py

請適當的修改 human_play.py，否則就會用預設的 model

要訓練 AI 來產生 model:
> python train.py

上面會產生 (best_policy.model and current_policy.model)：
  1) 可以修改 train.py, 裡面有一段被註解掉，它可以讀取 current_policy.model 繼續訓練
  2) 可以修改 train.py, 目前預設的棋盤大小可能不是你要的, 最原始是 6x6x4, 目前是 15x15x5

**Tips for training:**
1. It is good to start with a 6 * 6 board and 4 in a row. For this case, we may obtain a reasonably good model within 500~1000 self-play games in about 2 hours.
2. For the case of 8 * 8 board and 5 in a row, it may need 2000~3000 self-play games to get a good model, and it may take about 2 days on a single PC.

