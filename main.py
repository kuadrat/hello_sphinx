
class Main() :
    """
    This is documentation.
    """
    def foo(self) :
        """ The foo function. 
        This is very different from the :meth:`bar <hello_sphinx.main.Other.bar>`
        function.
        
        **Parameters**

        =====  =================================================================
        self   necessary; long text, maybe even spanning multiple lines. Would
               that work? Yes, but what happens if the text is even longer? 
               Do we get an annoying scrollbar? Can we avoid this?
        other  not known
        =====  =================================================================

        :confer:
            :class:`Main <hello_sphinx.main.Main>`
            :class:`Main <hello_sphinx.main.Main>`
            :class:`Main <hello_sphinx.main.Main>`

        :fooda boo da nooda:
            foo bar and so on
        """
        pass

class Other() :
    """ 
    Doc. The following line should be a literal block::
        
            +-+
            | |
            +-+
        .
            
    Is it?

    A list:

    * item 1
    * item 2

    An indented list:

        * item 1
        * item 2

    Barbara

    :see also:
        :meth:`bar <hello_sphinx.main.Other.bar>`
    """
    def bar(self) :
        """ The bar function. 
        
        :see also:

            :meth:`foo() <hello_sphinx.main.Main.foo>`
        """
        pass
