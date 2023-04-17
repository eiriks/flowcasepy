import json
import pytest

department = json.loads(open('tests/data/department.json').read())


print(department[0])

employee = {'user_id': '5702cc3069702d53c1008608', '_id': '5702cc3069702d53c1008608', 'id': '5702cc3069702d53c1008608', 'company_id': '531470a12f274fc51d000001', 'company_name': 'NoaIgnite prev MakingWaves', 'company_subdomains': ['noaignite'], 'company_group_ids': ['5c4f4d51f408a47ac96c47a7'], 'email': 'anders.haukvik@noaignite.com', 'external_unique_id': 'anders.haukvik', 'upn': 'anders.haukvik@noaignite.com', 'deactivated': False, 'deactivated_at': False, 'created_at': '2016-04-04T20:18:56.000Z', 'updated_at': '2021-06-21T08:25:28.320Z', 'role': 'consultant', 'roles': ['consultant'], 'role_allowed_office_ids': [], 'role_allowed_tag_ids': [], 'office_id': '56d7f60a69702d248e000008', 'office_name': 'Data Engineering', 'country_id': '531470a12f274fc51d000003', 'country_code': 'no', 'language_code': 'no', 'language_codes': ['no', 'int', 'dk', 'fi', 'se'], 'international_toggle': 'expand', 'preferred_download_format': 'pdf-from-word', 'masterdata_languages': ['no', 'int', 'dk', 'fi', 'se'], 'expand_proposals_toggle': True, 'selected_office_ids': [], 'include_officeless_reference_projects': False, 'selected_tag_ids': [], 'override_language_code': None, 'default_cv_template_id': '6267ee5dd9d1d50ff15bc253',
            'image': {
                'url': 'https://cvpartner-images.s3.eu-west-1.amazonaws.com/uploads/production/bruker/image/5702cc3069702d53c1008608/anders.haukvik.jpg?X-Amz-Expires=1200&X-Amz-Date=20230412T081807Z&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCWV1LXdlc3QtMSJGMEQCIAQkKuqlgKabHKV3IncLbepHmOUMbvaRaE7hJz6ypyPsAiBEenqNocPhH9%2B62a0aAL1bLDPb0sJJYEy8oC9aSn%2FsdCq4BQi2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDU3MTU4MDAxMDEzMiIMtpp8DPOP2oYSFrRvKowFWcNutnuOPa%2FplKKGEsaB1LPIaDZdedc0YZRr1MDmeuicCiFUG0Oo1uQPSlrYJrdNtiRcF8xE4e%2Fu40zCoR%2BiTn%2BjSnSWfu9MclXLXZddtsjpS%2FqjwhL4ciHpEFPBP%2BfrHDoiGrWydwuj%2FpITyoCf64rPwn7WyMyvelLNjASAFuld7777dTlLjJf%2Fg7SdizKXs080ieF1rDloM7AhlDY7w2Jehkd5%2Bbt0X5gpqwgaLycW0V0O6t5IZ41%2B9nQ15Vq5r%2FgSw152fo2zAPDyUseUgq8dZxsxh%2FPKgn%2BgC5axj0H7BXwXDKNZPp7PztY9Azpb19pFDKfrlqUiEU%2FXqdtPfkSIvUccZKiKH4Rs6VgMk4FByGAgRNUyrtI9GwKude6qP5FaAaiwJW9MFNaO%2BbV1AVcUOSaWDFyheqXGsuR%2B0lemPJzzt7zzEhp8KEEPE%2FftNQgNnpb4t4r0F2CkoFwduv1%2FhE9szR8O3i1P9CLHjPciN%2BW00j5FAlUyviMmTqJtsXRjH9eocPdKkn2gihA6BH6sTIgZsrF4OvsEe2ke3IgVY0B1DERy1pb73HBShq9bZVNwb6S3YvEgZ2AN0ZE3x7WyD799pItpm3KejN9WLBojXLNgCxDcAfSsReVSrsqbOdUq4%2FqrB8mxCiZVPWi%2BJBF0ugYOlj7SNYm6Fqc3c4h8XaKvHdkizpheADfv6FZP0T9Tupb6CUG9ykce%2BPIRr4rEKUiccTB82E63JI%2Fm2dzqi1YLAnZnTU11UABVSNn7Vt2jXXl58glG2mgv4OZ1W65%2BC%2FpbcoAMvKW%2FW3%2FhZcFrGN2PsJTOXm4cw49Csea%2FygiQ1MobvDNednRJvMqAB4sT6e3XKgesctp8mTDh9dihBjqyAXY%2BhCJZhL6lOjeO63Omnrx0EOB0iVNghVx7k7DSKle7Yjw58iVn%2FqTPIJm4EW%2BOrllOugyXoH2ns8gvOdkGvJsHEVerBsDc%2B%2FcEPEiYKh80wZjB%2Bw6cTkXU4Kh0UdHzixhkYfLAKltzOuO9pAFO1o3FXR5yKCk3Vy%2FBVb2h8mYv28SzwnEp1pls9vyEAs09TDTC9%2FMDHSB2QkOw32x9OyKMtziYUMtPWmnJwl3GT5yfmEM%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAYKFGSZ2KBIZVWJ7A%2F20230412%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-SignedHeaders=host&X-Amz-Signature=4136569c79ca7d76169065f3366052239c2ecc9c13f510b8766fe730252866f3',
                'thumb': {
                    'url': 'https://cvpartner-images.s3.eu-west-1.amazonaws.com/uploads/production/bruker/image/5702cc3069702d53c1008608/thumb_anders.haukvik.jpg?X-Amz-Expires=1200&X-Amz-Date=20230412T081807Z&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCWV1LXdlc3QtMSJGMEQCIAQkKuqlgKabHKV3IncLbepHmOUMbvaRaE7hJz6ypyPsAiBEenqNocPhH9%2B62a0aAL1bLDPb0sJJYEy8oC9aSn%2FsdCq4BQi2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDU3MTU4MDAxMDEzMiIMtpp8DPOP2oYSFrRvKowFWcNutnuOPa%2FplKKGEsaB1LPIaDZdedc0YZRr1MDmeuicCiFUG0Oo1uQPSlrYJrdNtiRcF8xE4e%2Fu40zCoR%2BiTn%2BjSnSWfu9MclXLXZddtsjpS%2FqjwhL4ciHpEFPBP%2BfrHDoiGrWydwuj%2FpITyoCf64rPwn7WyMyvelLNjASAFuld7777dTlLjJf%2Fg7SdizKXs080ieF1rDloM7AhlDY7w2Jehkd5%2Bbt0X5gpqwgaLycW0V0O6t5IZ41%2B9nQ15Vq5r%2FgSw152fo2zAPDyUseUgq8dZxsxh%2FPKgn%2BgC5axj0H7BXwXDKNZPp7PztY9Azpb19pFDKfrlqUiEU%2FXqdtPfkSIvUccZKiKH4Rs6VgMk4FByGAgRNUyrtI9GwKude6qP5FaAaiwJW9MFNaO%2BbV1AVcUOSaWDFyheqXGsuR%2B0lemPJzzt7zzEhp8KEEPE%2FftNQgNnpb4t4r0F2CkoFwduv1%2FhE9szR8O3i1P9CLHjPciN%2BW00j5FAlUyviMmTqJtsXRjH9eocPdKkn2gihA6BH6sTIgZsrF4OvsEe2ke3IgVY0B1DERy1pb73HBShq9bZVNwb6S3YvEgZ2AN0ZE3x7WyD799pItpm3KejN9WLBojXLNgCxDcAfSsReVSrsqbOdUq4%2FqrB8mxCiZVPWi%2BJBF0ugYOlj7SNYm6Fqc3c4h8XaKvHdkizpheADfv6FZP0T9Tupb6CUG9ykce%2BPIRr4rEKUiccTB82E63JI%2Fm2dzqi1YLAnZnTU11UABVSNn7Vt2jXXl58glG2mgv4OZ1W65%2BC%2FpbcoAMvKW%2FW3%2FhZcFrGN2PsJTOXm4cw49Csea%2FygiQ1MobvDNednRJvMqAB4sT6e3XKgesctp8mTDh9dihBjqyAXY%2BhCJZhL6lOjeO63Omnrx0EOB0iVNghVx7k7DSKle7Yjw58iVn%2FqTPIJm4EW%2BOrllOugyXoH2ns8gvOdkGvJsHEVerBsDc%2B%2FcEPEiYKh80wZjB%2Bw6cTkXU4Kh0UdHzixhkYfLAKltzOuO9pAFO1o3FXR5yKCk3Vy%2FBVb2h8mYv28SzwnEp1pls9vyEAs09TDTC9%2FMDHSB2QkOw32x9OyKMtziYUMtPWmnJwl3GT5yfmEM%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAYKFGSZ2KBIZVWJ7A%2F20230412%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-SignedHeaders=host&X-Amz-Signature=ba5724b9290321923ab4f8decf49eaefb2f204d3b9ddf5769d462cd0b494886f'
                },
                'fit_thumb': {
                    'url': 'https://cvpartner-images.s3.eu-west-1.amazonaws.com/uploads/production/bruker/image/5702cc3069702d53c1008608/fit_thumb_anders.haukvik.jpg?X-Amz-Expires=1200&X-Amz-Date=20230412T081807Z&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCWV1LXdlc3QtMSJGMEQCIAQkKuqlgKabHKV3IncLbepHmOUMbvaRaE7hJz6ypyPsAiBEenqNocPhH9%2B62a0aAL1bLDPb0sJJYEy8oC9aSn%2FsdCq4BQi2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDU3MTU4MDAxMDEzMiIMtpp8DPOP2oYSFrRvKowFWcNutnuOPa%2FplKKGEsaB1LPIaDZdedc0YZRr1MDmeuicCiFUG0Oo1uQPSlrYJrdNtiRcF8xE4e%2Fu40zCoR%2BiTn%2BjSnSWfu9MclXLXZddtsjpS%2FqjwhL4ciHpEFPBP%2BfrHDoiGrWydwuj%2FpITyoCf64rPwn7WyMyvelLNjASAFuld7777dTlLjJf%2Fg7SdizKXs080ieF1rDloM7AhlDY7w2Jehkd5%2Bbt0X5gpqwgaLycW0V0O6t5IZ41%2B9nQ15Vq5r%2FgSw152fo2zAPDyUseUgq8dZxsxh%2FPKgn%2BgC5axj0H7BXwXDKNZPp7PztY9Azpb19pFDKfrlqUiEU%2FXqdtPfkSIvUccZKiKH4Rs6VgMk4FByGAgRNUyrtI9GwKude6qP5FaAaiwJW9MFNaO%2BbV1AVcUOSaWDFyheqXGsuR%2B0lemPJzzt7zzEhp8KEEPE%2FftNQgNnpb4t4r0F2CkoFwduv1%2FhE9szR8O3i1P9CLHjPciN%2BW00j5FAlUyviMmTqJtsXRjH9eocPdKkn2gihA6BH6sTIgZsrF4OvsEe2ke3IgVY0B1DERy1pb73HBShq9bZVNwb6S3YvEgZ2AN0ZE3x7WyD799pItpm3KejN9WLBojXLNgCxDcAfSsReVSrsqbOdUq4%2FqrB8mxCiZVPWi%2BJBF0ugYOlj7SNYm6Fqc3c4h8XaKvHdkizpheADfv6FZP0T9Tupb6CUG9ykce%2BPIRr4rEKUiccTB82E63JI%2Fm2dzqi1YLAnZnTU11UABVSNn7Vt2jXXl58glG2mgv4OZ1W65%2BC%2FpbcoAMvKW%2FW3%2FhZcFrGN2PsJTOXm4cw49Csea%2FygiQ1MobvDNednRJvMqAB4sT6e3XKgesctp8mTDh9dihBjqyAXY%2BhCJZhL6lOjeO63Omnrx0EOB0iVNghVx7k7DSKle7Yjw58iVn%2FqTPIJm4EW%2BOrllOugyXoH2ns8gvOdkGvJsHEVerBsDc%2B%2FcEPEiYKh80wZjB%2Bw6cTkXU4Kh0UdHzixhkYfLAKltzOuO9pAFO1o3FXR5yKCk3Vy%2FBVb2h8mYv28SzwnEp1pls9vyEAs09TDTC9%2FMDHSB2QkOw32x9OyKMtziYUMtPWmnJwl3GT5yfmEM%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAYKFGSZ2KBIZVWJ7A%2F20230412%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-SignedHeaders=host&X-Amz-Signature=a17296bc05d07691fceb2a14e66864ac9a8f739425fd1adc685f8a380cf1f9e1'
                },
                'large': {
                    'url': 'https://cvpartner-images.s3.eu-west-1.amazonaws.com/uploads/production/bruker/image/5702cc3069702d53c1008608/large_anders.haukvik.jpg?X-Amz-Expires=1200&X-Amz-Date=20230412T081807Z&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCWV1LXdlc3QtMSJGMEQCIAQkKuqlgKabHKV3IncLbepHmOUMbvaRaE7hJz6ypyPsAiBEenqNocPhH9%2B62a0aAL1bLDPb0sJJYEy8oC9aSn%2FsdCq4BQi2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDU3MTU4MDAxMDEzMiIMtpp8DPOP2oYSFrRvKowFWcNutnuOPa%2FplKKGEsaB1LPIaDZdedc0YZRr1MDmeuicCiFUG0Oo1uQPSlrYJrdNtiRcF8xE4e%2Fu40zCoR%2BiTn%2BjSnSWfu9MclXLXZddtsjpS%2FqjwhL4ciHpEFPBP%2BfrHDoiGrWydwuj%2FpITyoCf64rPwn7WyMyvelLNjASAFuld7777dTlLjJf%2Fg7SdizKXs080ieF1rDloM7AhlDY7w2Jehkd5%2Bbt0X5gpqwgaLycW0V0O6t5IZ41%2B9nQ15Vq5r%2FgSw152fo2zAPDyUseUgq8dZxsxh%2FPKgn%2BgC5axj0H7BXwXDKNZPp7PztY9Azpb19pFDKfrlqUiEU%2FXqdtPfkSIvUccZKiKH4Rs6VgMk4FByGAgRNUyrtI9GwKude6qP5FaAaiwJW9MFNaO%2BbV1AVcUOSaWDFyheqXGsuR%2B0lemPJzzt7zzEhp8KEEPE%2FftNQgNnpb4t4r0F2CkoFwduv1%2FhE9szR8O3i1P9CLHjPciN%2BW00j5FAlUyviMmTqJtsXRjH9eocPdKkn2gihA6BH6sTIgZsrF4OvsEe2ke3IgVY0B1DERy1pb73HBShq9bZVNwb6S3YvEgZ2AN0ZE3x7WyD799pItpm3KejN9WLBojXLNgCxDcAfSsReVSrsqbOdUq4%2FqrB8mxCiZVPWi%2BJBF0ugYOlj7SNYm6Fqc3c4h8XaKvHdkizpheADfv6FZP0T9Tupb6CUG9ykce%2BPIRr4rEKUiccTB82E63JI%2Fm2dzqi1YLAnZnTU11UABVSNn7Vt2jXXl58glG2mgv4OZ1W65%2BC%2FpbcoAMvKW%2FW3%2FhZcFrGN2PsJTOXm4cw49Csea%2FygiQ1MobvDNednRJvMqAB4sT6e3XKgesctp8mTDh9dihBjqyAXY%2BhCJZhL6lOjeO63Omnrx0EOB0iVNghVx7k7DSKle7Yjw58iVn%2FqTPIJm4EW%2BOrllOugyXoH2ns8gvOdkGvJsHEVerBsDc%2B%2FcEPEiYKh80wZjB%2Bw6cTkXU4Kh0UdHzixhkYfLAKltzOuO9pAFO1o3FXR5yKCk3Vy%2FBVb2h8mYv28SzwnEp1pls9vyEAs09TDTC9%2FMDHSB2QkOw32x9OyKMtziYUMtPWmnJwl3GT5yfmEM%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAYKFGSZ2KBIZVWJ7A%2F20230412%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-SignedHeaders=host&X-Amz-Signature=4322b91e848524f4c11edacf42706be52e4a6352796a5fd1063517eaaf8109ac'
                },
                'small_thumb': {
                    'url': 'https://cvpartner-images.s3.eu-west-1.amazonaws.com/uploads/production/bruker/image/5702cc3069702d53c1008608/small_thumb_anders.haukvik.jpg?X-Amz-Expires=1200&X-Amz-Date=20230412T081807Z&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCWV1LXdlc3QtMSJGMEQCIAQkKuqlgKabHKV3IncLbepHmOUMbvaRaE7hJz6ypyPsAiBEenqNocPhH9%2B62a0aAL1bLDPb0sJJYEy8oC9aSn%2FsdCq4BQi2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDU3MTU4MDAxMDEzMiIMtpp8DPOP2oYSFrRvKowFWcNutnuOPa%2FplKKGEsaB1LPIaDZdedc0YZRr1MDmeuicCiFUG0Oo1uQPSlrYJrdNtiRcF8xE4e%2Fu40zCoR%2BiTn%2BjSnSWfu9MclXLXZddtsjpS%2FqjwhL4ciHpEFPBP%2BfrHDoiGrWydwuj%2FpITyoCf64rPwn7WyMyvelLNjASAFuld7777dTlLjJf%2Fg7SdizKXs080ieF1rDloM7AhlDY7w2Jehkd5%2Bbt0X5gpqwgaLycW0V0O6t5IZ41%2B9nQ15Vq5r%2FgSw152fo2zAPDyUseUgq8dZxsxh%2FPKgn%2BgC5axj0H7BXwXDKNZPp7PztY9Azpb19pFDKfrlqUiEU%2FXqdtPfkSIvUccZKiKH4Rs6VgMk4FByGAgRNUyrtI9GwKude6qP5FaAaiwJW9MFNaO%2BbV1AVcUOSaWDFyheqXGsuR%2B0lemPJzzt7zzEhp8KEEPE%2FftNQgNnpb4t4r0F2CkoFwduv1%2FhE9szR8O3i1P9CLHjPciN%2BW00j5FAlUyviMmTqJtsXRjH9eocPdKkn2gihA6BH6sTIgZsrF4OvsEe2ke3IgVY0B1DERy1pb73HBShq9bZVNwb6S3YvEgZ2AN0ZE3x7WyD799pItpm3KejN9WLBojXLNgCxDcAfSsReVSrsqbOdUq4%2FqrB8mxCiZVPWi%2BJBF0ugYOlj7SNYm6Fqc3c4h8XaKvHdkizpheADfv6FZP0T9Tupb6CUG9ykce%2BPIRr4rEKUiccTB82E63JI%2Fm2dzqi1YLAnZnTU11UABVSNn7Vt2jXXl58glG2mgv4OZ1W65%2BC%2FpbcoAMvKW%2FW3%2FhZcFrGN2PsJTOXm4cw49Csea%2FygiQ1MobvDNednRJvMqAB4sT6e3XKgesctp8mTDh9dihBjqyAXY%2BhCJZhL6lOjeO63Omnrx0EOB0iVNghVx7k7DSKle7Yjw58iVn%2FqTPIJm4EW%2BOrllOugyXoH2ns8gvOdkGvJsHEVerBsDc%2B%2FcEPEiYKh80wZjB%2Bw6cTkXU4Kh0UdHzixhkYfLAKltzOuO9pAFO1o3FXR5yKCk3Vy%2FBVb2h8mYv28SzwnEp1pls9vyEAs09TDTC9%2FMDHSB2QkOw32x9OyKMtziYUMtPWmnJwl3GT5yfmEM%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAYKFGSZ2KBIZVWJ7A%2F20230412%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-SignedHeaders=host&X-Amz-Signature=f4069f07afcf4a2c77f1e93836ec64974e7bdbb6c33d9c3877d97c31fa1ccd4c'
                }
},
    'name': 'Anders Haukvik', 'telephone': '91700331', 'default_cv_id': '5702cc3069702d53c1008609'}

# write a dataclass for employee


# List emploees that are about to be promoted js>ks>sr>principal


@pytest.mark.skip(reason="TDD")
def test_list_emploees_that_are_about_to_be_promoted():
    assert False


# List dept by time since highest edu was ended
@pytest.mark.skip(reason="TDD")
def test_list_dept_by_time_since_highest_edu_ended():
    assert False


# List dept by time since first project_expeirence was started
@pytest.mark.skip(reason="TDD")
def test_list_dept_by_time_since_first_project_expeirence_was_started():
    assert False


# List dept by times sinze last project_expeirence that was longer than 3 months
# (expected to filter out summer jobs, internships etc)

@pytest.mark.skip(reason="TDD")
def test_list_dept_by_time_sinze_last_project_expeirence_that_was_longer_than_3_months():
    assert False


# List department by time since last updated by user
@pytest.mark.skip(reason="TDD")
def test_list_department_by_time_since_last_updated_by_user():
    assert False


# group adpartment into 4 groups:
# 1. 0-1 years (junior)
# 2. >2 years (konsultant)
# 3. >5 years (senior)
# 4. >10 years (principal)
@pytest.mark.skip(reason="TDD")
def test_group_department_into_4_groups():
    assert False


# group department into 4 levels:
# • Level 1: 8 < years experience
# Selvstendige konsulenter med lang erfaring - over de siste 8 år som er relevant for det aktuelle området. Konsulenten har høyere utdanning, manglende utdanning kan kompenseres med lengre erfaring.
# • Level 2: 5-8 years experience
# Selvstendige konsulenter med lengre erfaring  over de siste 5-8 år som er relevant for det aktuelle området. Konsulenten har høyere utdanning, manglende utdanning kan kompenseres med lengre erfaring.
# • Level 3: 2 - <5 years experience
# Selvstendige konsulenter med minimum - over de siste 2 års erfaring som er relevant for det aktuelle området. Konsulenten har høyere utdannelse, anglende utdanning kan kompenseres med lengre erfaring
# • Level 4: < 2 years experience
# Konsulenter med under 2 års erfaring som er relevant for det aktuelle området. Konsulenten har høyere utdannelse, minimum mastergrad, manglende utdanning kan kompenseres med lengre erfaring. "

@pytest.mark.skip(reason="TDD")
def test_group_department_into_4_levels():
    assert False
