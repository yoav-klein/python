# additionalProperties

This keyword is used to impose validation on any property in the object that is not matched by the
`properties` or `patternProperties` keywords. 

Setting it to `false` will forbid any additional property. You can also set it to an object and apply
any sort of condition on it, such as:

```
{
    "..."
    "additionalProperties": {
        "type": "string"
    }
}
```

This will force that any additional property must be a string.