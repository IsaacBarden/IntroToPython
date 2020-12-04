#Very short example of pakages, make sure you run the module you want to use before you import it
import ExampleModule
from ExamplePackage.PackageModule import square_root

num = 5
num = ExampleModule.square(num)
print(num)
num = square_root(num)
print(num)