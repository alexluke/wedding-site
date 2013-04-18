require.config
    paths:
        jquery: '../../components/jquery/jquery'
        bootstrapTransition: '../../components/sass-bootstrap/js/bootstrap-transition'
        bootstrapCollapse: '../../components/sass-bootstrap/js/bootstrap-collapse'
    shim:
        bootstrapTransition: ['jquery']
        bootstrapCollapse: ['jquery', 'bootstrapTransition']
    deps: ['bootstrapCollapse']
