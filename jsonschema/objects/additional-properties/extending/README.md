# Extending with additionalProperties

The problem here is that the `additionalProperties` only recognizes `properties` 
in its own sub-schema. So in this example, the `additionalProperties` only "sees" the 
`street_address`, `city`, `state` properties, not the `type` property.

So both the files here will fail, one because of the `additionalProperties` and one because of the
`required`.