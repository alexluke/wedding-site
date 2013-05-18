define [
    'jquery'
    'bootstrapCollapse'
], ($) ->
    $('input[name=attending]').on 'change', ->
        $this = $ this
        $('.collapse.in').collapse 'hide'
        target = $ $this.data 'target'
        target.collapse 'show'

