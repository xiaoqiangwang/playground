Record
------

Record has the following attibutes:

  name 
    Record name.

  rtyp
    Record type.

  field
    Dictionary of record fields.

  info
    Dictionary of record infos.

  alias
    List of aliased names.

Database
--------

Database derives from OrderedDict. The key is the record name and the value the *Record* instance.
