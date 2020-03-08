from django.core.management.base import BaseCommand, CommandError
from draft_app.models import *
from battlerite_draft import settings
from datetime import date

import requests
from io import BytesIO
from django.core.files.base import ContentFile

class Command(BaseCommand):

    def handle(self, *args, **options):
        champions = [
            ('Bakko', 'Melee', 'https://gamepedia.cursecdn.com/battlerite_gamepedia_en/1/1d/Bakko_Portrait.png?version=83f8a77eaaaa65c2f7a4e4dcd61fc3cb'),
            ('Croak', 'Melee', 'https://gamepedia.cursecdn.com/battlerite_gamepedia_en/f/f0/Croak_Portrait.png?version=385db394cd8388a3a6958baac3dadd72'),
            ('Freya', 'Melee', 'https://gamepedia.cursecdn.com/battlerite_gamepedia_en/f/fb/Freya_Portrait.png?version=843b4e9b0ffdcd3d00aac1feeee7423f'),
            ('Raigon', 'Melee', 'https://gamepedia.cursecdn.com/battlerite_gamepedia_en/c/c1/Raigon_Portrait.png?version=63e1bbbb45fe97c50655a575c6025f02'),
            ('Rook', 'Melee', 'https://gamepedia.cursecdn.com/battlerite_gamepedia_en/3/3a/Rook_Portrait.png?version=926f9679b030a6fed5faf71737919324'),
            ('Ruh Kaan', 'Melee', 'https://gamepedia.cursecdn.com/battlerite_gamepedia_en/e/e5/Ruh_Kaan_Portrait.png?version=38d38c0c604b4dce1a5f135fba922acf'),
            ('Shifu', 'Melee', 'https://gamepedia.cursecdn.com/battlerite_gamepedia_en/d/d9/Shifu_Portrait.png?version=1e40211f397121bc1404d46d23655c87'),
            ('Thorn', 'Melee', 'https://gamepedia.cursecdn.com/battlerite_gamepedia_en/7/75/Thorn_Portrait.png?version=01545470393bd4134c28910b2352af88'),
            ('Alysia', 'Ranged', 'https://gamepedia.cursecdn.com/battlerite_gamepedia_en/6/6d/Alysia_Portrait.png?version=8ba4433e2c2977f3c76be3e81b92d4ae'),
            ('Ashka', 'Ranged', 'https://gamepedia.cursecdn.com/battlerite_gamepedia_en/3/33/Ashka_Portrait.png?version=4c056242f3c8db48e562ab21a154e360'),
            ('Destiny', 'Ranged', 'https://gamepedia.cursecdn.com/battlerite_gamepedia_en/e/ec/Destiny_Portrait.png?version=5de887858d6bdefe8ecc998cee35aeda'),
            ('Ezmo', 'Ranged', 'https://gamepedia.cursecdn.com/battlerite_gamepedia_en/6/64/Ezmo_Portrait.png?version=0c1631901e218475c9e9c03c2a6ec835'),
            ('Iva', 'Ranged', 'https://gamepedia.cursecdn.com/battlerite_gamepedia_en/d/dc/Iva_Portrait.png?version=9de636c7e481df2cb81416bafcafcd16'),
            ('Jade', 'Ranged', 'https://gamepedia.cursecdn.com/battlerite_gamepedia_en/7/7e/Jade_Portrait.png?version=0117636f708b456fe5d709a93e961636'),
            ('Jumong', 'Ranged', 'https://gamepedia.cursecdn.com/battlerite_gamepedia_en/7/74/Jumong_Portrait.png?version=70beae655c63cf2a862644732399ea2e'),
            ('Taya', 'Ranged', 'https://gamepedia.cursecdn.com/battlerite_gamepedia_en/2/26/Taya_Portrait.png?version=53ac4514842df795875215fd3de32382'),
            ('Varesh', 'Ranged', 'https://gamepedia.cursecdn.com/battlerite_gamepedia_en/2/20/Varesh_Portrait.png?version=d1a617e0f26752eade1272b750829def'),
            ('Shen Rao', 'Ranged', 'https://www.battleritebuilds.com/assets/img/c0e3f68a87771064ab57d6cd36430ed9.png'),
            
            ('Blossom', 'Support', 'https://gamepedia.cursecdn.com/battlerite_gamepedia_en/9/94/Blossom_Portrait.png?version=1b86c0e7a35a6a7186928c66458719ab'),
            ('Lucie', 'Support', 'https://gamepedia.cursecdn.com/battlerite_gamepedia_en/8/8e/Lucie_Portrait.png?version=e164a75293acf803a2b02b57c7f98b8e'),
            ('Oldur', 'Support', 'https://gamepedia.cursecdn.com/battlerite_gamepedia_en/0/0e/Oldur_Portrait.png?version=809fb808e881f9db35da08f7832b6a3c'),
            ('Pearl', 'Support', 'https://gamepedia.cursecdn.com/battlerite_gamepedia_en/0/05/Pearl_Portrait.png?version=d8f4144026b5197eae3dcc511ee01356'),
            ('Pestilus', 'Support', 'https://gamepedia.cursecdn.com/battlerite_gamepedia_en/f/f2/Pestilus_Portrait.png?version=dd3ac86d64d17ab1aad2b067c9408814'),
            ('Poloma', 'Support', 'https://gamepedia.cursecdn.com/battlerite_gamepedia_en/6/64/Poloma_Portrait.png?version=864a5478123395abec4b04be9c9a1078'),
            ('Sirius', 'Support', 'https://gamepedia.cursecdn.com/battlerite_gamepedia_en/4/42/Sirius_Portrait.png?version=5e05031af80d879ed53309858db02bf4'),
            ('Zander', 'Support', 'https://gamepedia.cursecdn.com/battlerite_gamepedia_en/a/a2/Zander_Portrait.png?version=ef701cd4e850d25cf04d4b1ff9ce6717'),
            ('Ulric', 'Support', 'https://cdn.battlerite.com/blog/2018/09/28115039/UlricPortrait.jpg'),
            
        ]
        l = []

        for c in champions:
            name, role, image_url = c
            request = requests.get(image_url)
            image_file = request.content
            file_ = BytesIO(image_file)
            c_file = ContentFile(file_.getvalue())
            def get_fmt(link):
                if 'png' in link:
                    return 'png'
                elif 'jpg' in link:
                    return 'jpg'
                elif 'jpeg' in link:
                    return 'jpeg'
            fmt = get_fmt(image_url)
            c_file.name = f'{name}.{fmt}'
            c = Champion.objects.create(name=name, role=role, picture=c_file)
            print(c, c.picture)
        
        #Champion.objects.bulk_create(l)