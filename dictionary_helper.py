from uuid import UUID
from common.required import Required

class DictionaryHelper:

    @staticmethod
    def find_value(
        
        dictionary      : "dict",
        key             : "str",
        is_Required     : "bool"    = True, # If required and no default value / None is given, raises exception 
        default_value   : "object"  = None

        ) -> "object": 

        __class__.is_dictionary(dictionary)

        if (key not in dictionary 
            and is_Required 
            and default_value is None):
            
            raise(
                ValueError(
                    f"Required key: {key} not found in dictionary"))

        if key not in dictionary:
            return default_value

        return dictionary[key]

    @staticmethod
    def is_dictionary(
        
        input_dictionary    : "dict",
        raise_exception     : "bool" = True # Optional default value is True
        
        ) -> "bool":

        flag = True
        if type(input_dictionary) is not dict:
            flag = False
            
            if raise_exception:
                raise TypeError(
                    "Input must be dict type")
        
        return flag

    @staticmethod
    def find_required_uuid(
        
        input_dictionary    : "dict",
        key                 : "str"

        ) -> "UUID":

        return UUID(
            DictionaryHelper.find_value(
                input_dictionary, 
                key, 
                True)
            )

    @staticmethod
    def find_required_string(

            input_dictionary    : "dict",
            key                 : "str",
            strip_string        : "bool" = True

        ):

        return Required.string_required(
            DictionaryHelper.find_value(
                input_dictionary,
                key,
                True),
            key,
            strip_string)
