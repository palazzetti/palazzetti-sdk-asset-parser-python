# Palazzetti SDK - Asset Parser

## Library to detect capabilities of Palazzetti's product based on static and dynamic data

Requires Python 3.6 and uses semver.

```python
import palazzetti_sdk_asset_parser as psap

def main():

    asset_parser = psap.AssetParser(get_alls={"STATUS":0}, get_stdt={"FAN2TYPE":3})
    asset_capabilities = asset_parser.parsed_data

    if (asset_capabilities.flag_has_fan): print("Product has main fan")

    if (asset_capabilities.value_product_is_on): print("Product is ON!")
    else: print("Product is OFF!")

main()
```