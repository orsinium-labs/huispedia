# huispedia

Python library to get information about houses from [huispedia.nl](https://huispedia.nl/).

**DISCLAIMER**: this is not an official API and doesn't use one. The script is provided as is (see the LICENSE) and for personal usage only. Please, contact the huispedia team (Huispedia BV) if you need a stable API for extensive or commercial usage.

## Installation

```bash
python3 -m pip install huispedia
```

## Usage

```python
import huispedia
houses = huispedia.get_houses(price_max=295000, con_year_min=1970)
print(houses[0])
```

Output example (anonymized, just in case):

```python
{
 'id': '...',
 'street': 'Examplestraat',
 'street_slug': 'examplestraat',
 'hnum': '13',
 'hchar': 'A',
 'city_name': 'Example',
 'city_slug': 'example',
 'postcode': '1234AB',
 'woonoppervlakte': '13',
 'perceeloppervlakte': '13',
 'aantal_kamers': '4',
 'bouwjaar': '1984',
 'object_type': 'woonhuis',
 'img_src': 'example.jpg',
 'status': 'TE KOOP',
 'status_updated_at': '12345678',
 'status_updated_by': 'REALTOR',
 'price_sale': '265000',
 'price_rent': '0',
 'price_search': '265000',
 'price_min_bid': '0',
 'price_aot_indication': '0',
 'price_m2': '1234',
 'price_valuation': '265000',
 'lat': '52.485558',
 'lon': '4.658634',
 'user_id': '0',
 'user_firstname': '',
 'office_name': 'Example Makelaar',
 'user_picture': '',
 'office_id': '123',
 'office_logo': 'id_123.png',
 'show_user_info': '1',
 'available_on_term_at': '0',
 'open_house_date': '0',
 'counts_images': '42',
 'counts_images360': '0',
 'counts_floorplans': '3',
 'counts_videos': '0',
 'inside': '1',
}
```
