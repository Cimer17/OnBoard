def main(contacts, id):
    vcf_file = f'contact/{str(id)}.vcf'
    vcard_list = []
    for phone, name in contacts.items():
        first_name, last_name = name.split(' ') if len(name.split(' ')) > 1 else (name, '')
        vcard_list.append(make_vcard(first_name, last_name, phone))
    write_vcard(vcf_file, vcard_list)

def make_vcard(
        first_name,
        last_name,
        phone):
    return [
        'BEGIN:VCARD',
        'VERSION:3.0',
        f'N:{last_name};{first_name}',
        f'TEL;WORK;VOICE:{phone}',
        'END:VCARD'
    ]

def write_vcard(f, vcard_list):
    with open(f, 'w', encoding='UTF-8') as f:
        for vcard in vcard_list:
            f.writelines([l + '\n' for l in vcard])
            f.write('\n')

if __name__ == "__main__":
    main()