1. By default are django signals executed synchronously or asynchronously? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

=> Django signals by default run synchronously. This means that once the signal is sent, it executes the receiver functions immediately in the same thread where it was sent, before any further code execution could continue.

Code Example: [Question 1](question_1.py)

2.  Do django signals run in the same thread as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

=> Yes, Django signals run in the same thread as the caller. Meaning the receiver functions of a signal run in the same thread that invoked the signal.

Code Example: [Question 2](question_2.py)

3. By default do django signals run in the same database transaction as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

=> Django signals run by default inside the same database transaction as the caller. As a result, in case a signal is dispatched in the course of saving a model, the signal handlers will run within the context of that same transaction. If the transaction gets rolled back, then the effect of the signal handlers will get rolled back with it.

Code Example: [Question 3](question_3.py)

4. An instance of the Rectangle class requires length:int and width:int to be initialized.
We can iterate over an instance of the Rectangle class 
When an instance of the Rectangle class is iterated over, we first get its length in the format: {'length': <VALUE_OF_LENGTH>} followed by the width {width: <VALUE_OF_WIDTH>}

Code Example: [Custom Class](custom_class.py)
