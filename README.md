# exercises

1. **YAML Exercise** - 
function that receives a YAML and an additional configuration for the YAML. 
In the function, the additional config is appended to the existing YAML accordingly. 
If the same key shows up in the YAML and the additional config, 
the new value will not override the existing value but instead will create a list consisting of both values. 

2. **Requirements files Exercise** - 
function that receives a requirements file and creates a string consisting of all of its libraries. 
If the requirements file includes more requirements files inside it,  
their libraries will be attached to the string as well, until there are no more requirements files left.