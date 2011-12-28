# This is a work in progress. Don't use #
# ------- #

# Django Stylus

django-stylus lets you to integrate [Stylus](http://learnboost.github.com/stylus/) in your Django projects. 
django-stylus is based on monokrome's `django-cafe` from https://github.com/monokrome/django-cafe

## Install

	git clone https://github.com/lusentis/django-stylus/
	python setup.py install

A pypi package will be available when `django-stylus` will be _stable_.

## Setup

1.	Install stylus command line
2.	Add `stylus` to your `settings.INSTALLED_APPS`

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

