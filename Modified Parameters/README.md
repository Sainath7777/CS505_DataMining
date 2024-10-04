Modify Parameters to The Models with Neural Networks (20 Points)
Please submit the screen dumps

Showing the results

Make a Copy of the file:

tutorial05_different_approaches_to_define_neural_networks_keras.ipynb

1.- Do the following modifications:

model.compile(optimizer='SGD',loss='categorical_crossentropy', metrics=['accuracy']) # compiling the model

Train model and execute loss = model.evaluate(X_test, Y_oh_test, verbose=0)  print screen dumps

model.compile(optimizer='RMSprop'Links to an external site.'',loss='categorical_crossentropy', metrics=['accuracy']) # compiling the model

Train model and execute loss = model.evaluate(X_test, Y_oh_test, verbose=0)  print screen dumps

model.compile(optimizer='AdadeltaLinks to an external site.',loss='categorical_crossentropy', metrics=['accuracy']) # compiling the model

Train model and execute loss = model.evaluate(X_test, Y_oh_test, verbose=0)  print screen dumps

2.- Do the following Modifications

model.compile(optimizer='adam',loss='BinaryCrossentropyLinks to an external site.', metrics=['accuracy']) # compiling the model

Train model and execute loss = model.evaluate(X_test, Y_oh_test, verbose=0)  print screen dumps

model.compile(optimizer='adam',loss='CategoricalFocalCrossentropy', metrics=['accuracy']) # compiling the model

Train model and execute loss = model.evaluate(X_test, Y_oh_test, verbose=0)  print screen dumps

model.compile(optimizer='adam',loss='SparseCategoricalCrossentropy', metrics=['accuracy']) # compiling the model

Train model and execute loss = model.evaluate(X_test, Y_oh_test, verbose=0)  print screen dumps



------------------------------SUMMARY OF THE CHANGES MADE TO THE PARAMETERS--------------------------------------------------

Optimizer variations:

We created a list of optimizers to test: ['SGD', 'RMSprop', 'Adadelta'].
In a loop, we create a new model for each optimizer and call train_and_evaluate with the current optimizer and 'categorical_crossentropy' as the loss function.


Loss function variations:

We created a list of loss functions to test: ['BinaryCrossentropy', 'CategoricalFocalCrossentropy', 'SparseCategoricalCrossentropy'].
In a loop, we create a new model for each loss function and call train_and_evaluate with 'adam' as the optimizer and the current loss function.
For 'SparseCategoricalCrossentropy', we use non-one-hot encoded labels (Y_test instead of Y_oh_test) when evaluating the model.



The main changes are in the train_and_evaluate function, which now takes the optimizer and loss function as parameters, allowing us to easily test different combinations.
These modifications allow us to systematically test different optimizers and loss functions while keeping the model architecture constant. This approach helps in understanding how these hyperparameters affect the model's performance on the Iris dataset.
