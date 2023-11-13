## Set up virtual environment

As always, create a Python virtual environment, first:

```
$ mkdir pytorch-learning
$ cd pytorch-learning
$ python3 -m venv .venv
$ source .venv/bin/activate
(.venv) $ pip install wheel
(.venv) $ 
```
## Install Pytorch

Go to https://pytorch.org. 
Click on "Get Started" in top menu. 
Choose "Start Locally"
Select the options for your setup. I chose:

* Stable
* Linux
* Pip
* Python
* CPU

The website then give me the command to run that will install Pytorch. In my case, the command is:

```text
(.venv) $ pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
```

Other packages needed are: matplotlib and Jupyter.

```text
(.venv) $ pip install matplotlib
(.venv) $ pip install jupyterlab
```

## Data sets

Use pre-loaded example data sets. Pytorch classes to use are:

*Dataset* and *DataLoader*

Preloaded data sets:

* https://pytorch.org/vision/stable/datasets.html
* https://pytorch.org/text/stable/datasets.html
* https://pytorch.org/audio/stable/datasets.html




