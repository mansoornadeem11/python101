class Required:

    @staticmethod
    def get_string(
        
        input_string    : "str",
        variable_name   : "str",            #Name of the input string being passed as the first argument
        strip_string    : "bool" = False    #Applies left right strip to string

        ) -> "str":
        
        if input_string is not None:
            __class__.must_be_of_type(
                input_string, 
                variable_name, 
                str)
            
            if strip_string:
                input_string = (
                    input_string.strip()
                    )

        return input_string
    
    @staticmethod
    def string_required(
        
        input_string    : "str",
        variable_name   : "str",            #Name of the input string being passed as the first argument
        strip_string    : "bool" = False    #Applies left right strip to string

        ) -> "str":

        error = f"{variable_name} (string) required"
        
        input_string = __class__.get_string(
            input_string,
            variable_name,
            strip_string
        )

        if (input_string is None or
            input_string == ""):

            raise(ValueError(error))

        return input_string

    @staticmethod
    def must_be_of_type(

        input_variable,
        input_variable_name,
        input_variable_type
    ):

        if type(input_variable) != input_variable_type:
            raise ValueError(
                f"Expects {input_variable_name} to be of type {input_variable_type}")

        return input_variable