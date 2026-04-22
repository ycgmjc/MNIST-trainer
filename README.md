<h1>MNIST Trainer</h1>
<p>This is a simple Neural Network trainer that utilizes the MNIST Dataset.</p>

<h3>Description</h3>
<ul>
    <li><strong>Loader.py</strong>: Responsible for loading in the MNIST dataset and preparing it for training.</li>
    <li><strong>Models.py</strong>: Holds Neural Network models to use for training.</li>
    <li><strong>trainer.py</strong>: The actual trainer used to train the neural network.</li>
    <li><strong>requirements.txt</strong>: The requirements for running the trainer.</li>
    <li><strong>/Exps</strong>: The directory where each training result is saved.</li>
    <li><strong>/dataset</strong>: The directory where the MNIST dataset should be in.</li>
</ul>

<h3>How to use</h3>
<ol>
    <li>Make sure you have Python and the requirements installed.<br>
        To install all requirements, run <code>pip install -r requirements.txt</code></li>
    <li>(Optional) Change configs and hyperparameters in <code>trainer.py</code>.</li>
    <li>Run the trainer: <code>python trainer.py</code></li>
    <li>The trained module will be saved in <code>/Exps</code>.</li>
</ol>
