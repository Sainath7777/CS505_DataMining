Modify Parameters to The Models withe Neural Networks (20 Points)
Pease submit the screen dumps

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
