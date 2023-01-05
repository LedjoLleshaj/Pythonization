# Virtual environments

We shouldn't run pip3 install XXXXXX immediately because it will add the package in the global environment. We should create a virtual environment first and then install the package in the active virtual environment.

But different libraries may need different versions of Python. So, we need to create different virtual environments for different libraries. We can do this by running the following command:

```
python3 -m venv <name of the virtual environment>
```

```
python3 -m venv .venv
```

This way in each venv we can have different dependencies that our project needs. We can activate the virtual environment by running the following command:

```
source <name of the virtual environment>/bin/activate
```

```
source .venv/bin/activate
```

To deactivate the virtual environment, we can run the following command:

```
deactivate
```

To check the list of packages that are installed in the virtual environment, we can run the following command:

```
pip3 list
```

# Requirements.txt

We can also create a requirements.txt file that contains all the dependencies that our project needs. We can create this file by running the following command:

```
pip3 freeze > requirements.txt
```

To use an existing requirements.txt file, we can run the following command:

```
pip3 install -r requirements.txt
```

With this file we don't have to install the packages one by one. We can just run the above command and all the packages will be installed and also there is no need to commit the packages in the repository.

# To install a specific version of a package

We can install a specific version of a package by running the following command:

```
pip3 install <package name>==<version>
```

```
pip3 install requests==2.0
```

To upgrade a package to a specific version, we can run the following command:

```
pip3 install <package name>==<version> --upgrade
```

```
pip3 install requests==2.0 --upgrade
```

Or

```
pip3 install  -U requests
```
