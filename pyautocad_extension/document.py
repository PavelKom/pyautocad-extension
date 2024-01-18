


class AcadDocument(object):
    def __init__(self, template="", create_new=True):
        self.me = None
        if create_new:
            from .application import acad_app
            self.me = acad_app.create_doc(template)

    def __eq__(self, other):
        return self.me == other.me

    @staticmethod
    def from_app(doc):
        _doc = AcadDocument(create_new=False)
        _doc.me = doc
        return _doc

    def activate(self):
        """
        Makes the specified drawing active
        """
        self.me.Activate()

    @property
    def active(self) -> bool:
        """
        Determines if the document is the active document for the session
        """
        return self.me.Active

    @property
    def active_dim_style(self):  # As AcadDimStyle
        """
        Specifies the active dimension style
        """
        return self.me.ActiveDimStyle

    @active_dim_style.setter
    def active_dim_style(self, value):
        self.me.ActiveDimStyle = value

    @property
    def active_layer(self):  # As AcadLayer
        """
        Specifies the active layer
        """
        return self.me.ActiveLayer

    @active_layer.setter
    def active_layer(self, value):
        self.me.ActiveLayer = value

    @property
    def active_layout(self):  # As AcadLayout
        """
        Specifies the active layout
        """
        return self.me.ActiveLayout

    @active_layout.setter
    def active_layout(self, value):
        self.me.ActiveLayout = value

    @property
    def active_linetype(self):  # As AcadLineType
        """
        Specifies the active linetype for the drawing
        """
        return self.me.ActiveLinetype

    @active_linetype.setter
    def active_linetype(self, value):
        self.me.ActiveLinetype = value

    @property
    def active_material(self):  # As AcadMaterial
        """
        """
        return self.me.ActiveMaterial

    @active_material.setter
    def active_material(self, value):
        self.me.ActiveMaterial = value

    @property
    def active_pviewport(self):  # As AcadPViewport
        """
        Specifies the active paper space viewport for the drawing
        """
        return self.me.ActivePViewport

    @active_pviewport.setter
    def active_pviewport(self, value):
        self.me.ActivePViewport = value

    @property
    def active_selection_set(self):  # As AcadSelectionSet
        """
        Gets the active selection set for the drawing
        """
        return self.me.ActiveSelectionSet

    @property
    def active_space(self):  # As AcActiveSpace
        """
        Toggles the active space between paper space and model space
        """
        return self.me.ActiveSpace

    @active_space.setter
    def active_space(self, value):
        self.me.ActiveSpace = value

    @property
    def active_text_style(self):  # As AcadTextStyle
        """
        Specifies the active text style for the drawing
        """
        return self.me.ActiveTextStyle

    @active_text_style.setter
    def active_text_style(self, value):
        self.me.ActiveTextStyle = value

    @property
    def active_UCS(self):  # As AcadUCS
        """
        Specifies the active UCS for the drawing
        """
        return self.me.ActiveUCS

    @active_UCS.setter
    def active_UCS(self, value):
        self.me.ActiveUCS = value

    @property
    def active_viewport(self):  # As AcadViewport
        """
        Specifies the active viewport for the drawing
        """
        return self.me.ActiveViewport

    @active_viewport.setter
    def active_viewport(self, value):
        self.me.ActiveViewport = value

    @property
    def app(self):  # As AcadViewport
        """
        Gets the Application object
        Kinda sus
        """
        return self.me.Application

    def audit_info(self, fix_err: bool):
        """
        Evaluates the integrity of the drawing
        """
        self.me.AuditInfo(fix_err)

    @property
    def blocks_coll(self):  # As AcadBlocks
        """
        Gets the Blocks collection for the drawing
        """
        return self.me.Blocks





    """
    events:
        Activate
        BeginClose
        BeginCommand
        BeginDocClose
        BeginDoubleClick
        BeginLisp
        BeginPlot
        BeginRightClick
        BeginSave
        BeginShortcutMenuCommand
        BeginShortcutMenuDefault
        BeginShortcutMenuEdit
        BeginShortcutMenuGrip
        BeginShortcutMenuOsnap
    """






