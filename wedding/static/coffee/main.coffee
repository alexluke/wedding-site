require.config
    paths:
        jquery: '../../components/jquery/jquery'
        bootstrapTransition: '../../components/sass-bootstrap/js/bootstrap-transition'
        bootstrapCollapse: '../../components/sass-bootstrap/js/bootstrap-collapse'
        bootstrapCarousel: '../../components/sass-bootstrap/js/bootstrap-carousel'
    shim:
        bootstrapTransition: ['jquery']
        bootstrapCollapse: ['jquery', 'bootstrapTransition']
        bootstrapCarousel: ['jquery']
    deps: ['bootstrapCollapse', 'bootstrapCarousel']

require [
    'rsvp'
]
