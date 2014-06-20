PIPELINE_CSS = {
    'bootstrap': {
        'source_filenames': (
            'css/bootstrap.css',
            'css/bootstrap-theme.css',
        ),

        'output_filename': 'css/bootstrap.min.css',
    },

    'site': {
        'source_filenames': (
            'less/site.less',
        ),

        'output_filename': 'css/site.min.css',
    },
}


PIPELINE_JS = {
    'jquery': {
        'source_filenames': (
            'js/jquery-2.1.1.js',
        ),

        'output_filename': 'js/jquery.min.js',
    },

    'bootstrap': {
        'source_filenames': (
            'js/boostrap.js',
        ),

        'output_filename': 'js/bootstrap.min.js',
    },

    'site': {
        'source_filenames': (
            'coffee/site.coffee',
        ),

        'output_filename': 'js/site.min.js',
    },
}

PIPELINE_COMPILERS = (
    'pipeline.compilers.less.LessCompiler',
    'pipeline.compilers.coffee.CoffeeScriptCompiler',
)
