# Django Stylus

django-stylus lets you to integrate [Stylus](http://learnboost.github.com/stylus/) in your Django projects. 
django-stylus is based on monokrome's `django-cafe` from https://github.com/monokrome/django-cafe

## Install
	
	easy_install django-stylus

or

	git clone
	python setup.py install

## Setup

1.	Install stylus command line
2.	Add `stylus` to your `settings.INSTALLED_APPS


    INSTALLED_APPS = (
      ...
      "stylus", 
      ...      
    ) 


## Settings

### STYLUS_ROOT

Default: `STATIC_ROOT/_css/`

### STYLUS_OUTPUT_DIR

Default: `compiled`

### STYLUS_CACHE_TIME

Default: `3600`

### STYLUS_BIN

Default: `"stylus"`

### STYLUS_PARAMS

Default: `""`

