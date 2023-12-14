


(function () {
  'use strict'; // Allow Global access

  window.VectorMap = VectorMap;
  var defaultColors = {
    markerColor: '#23b7e5',
    // the marker points
    bgColor: 'transparent',
    // the background
    scaleColors: ['#878c9a'],
    // the color of the region in the serie
    regionFill: '#bbbec6', // the base region color
  };

  function VectorMap(element, seriesData, markersData) {
    if (!element || !element.length) return;
    var attrs = element.data(),
      mapHeight = attrs.height || '300',
      options = {
        markerColor: attrs.markerColor || defaultColors.markerColor,
        bgColor: attrs.bgColor || defaultColors.bgColor,
        scale: attrs.scale || 1,
        scaleColors: attrs.scaleColors || defaultColors.scaleColors,
        regionFill: attrs.regionFill || defaultColors.regionFill,
        mapName: attrs.mapName || 'world_mill_en',
      };
    element.css('height', mapHeight);
    init(element, options, seriesData, markersData);

    function init($element, opts, series, markers) {
      $element.vectorMap({
        map: opts.mapName,
        backgroundColor: opts.bgColor,
        zoomMin: 1,
        zoomMax: 8,
        zoomOnScroll: false,
        regionStyle: {
          initial: {
            fill: opts.regionFill,
            'fill-opacity': 1,
            stroke: 'none',
            'stroke-width': 1.5,
            'stroke-opacity': 1,
          },
          hover: {
            'fill-opacity': 0.8,
          },
          selected: {
            fill: 'blue',
          },
          selectedHover: {},
        },
        focusOn: {
          x: 0.4,
          y: 0.6,
          scale: opts.scale,
        },
        markerStyle: {
          initial: {
            fill: opts.markerColor,
            stroke: opts.markerColor,
          },
        },
        onRegionLabelShow: function onRegionLabelShow(e, el, code) {
          if (series && series[code]) el.html(el.html() + ': ' + series[code] + ' visitors');
        },
        markers: markers,
        series: {
          regions: [
            {
              values: series,
              scale: opts.scaleColors,
              normalizeFunction: 'polynomial',
            },
          ],
        },
      });
    } // end init
  }
})(); // BOOTGRID
// -----------------------------------

(function () {
  'use strict';

  $(initBootgrid);

  function initBootgrid() {
    if (!$.fn.bootgrid) return;
    $('#bootgrid-basic').bootgrid({
      templates: {
        // templates for BS4
        actionButton: '<button class="btn btn-secondary" type="button" title="{{ctx.text}}">{{ctx.content}}</button>',
        actionDropDown:
          '<div class="{{css.dropDownMenu}}"><button class="btn btn-secondary dropdown-toggle dropdown-toggle-nocaret" type="button" data-toggle="dropdown"><span class="{{css.dropDownMenuText}}">{{ctx.content}}</span></button><ul class="{{css.dropDownMenuItems}}" role="menu"></ul></div>',
        actionDropDownItem: '<li class="dropdown-item"><a href="" data-action="{{ctx.action}}" class="dropdown-link {{css.dropDownItemButton}}">{{ctx.text}}</a></li>',
        actionDropDownCheckboxItem: '<li class="dropdown-item"><label class="dropdown-item p-0"><input name="{{ctx.name}}" type="checkbox" value="1" class="{{css.dropDownItemCheckbox}}" {{ctx.checked}} /> {{ctx.label}}</label></li>',
        paginationItem: '<li class="page-item {{ctx.css}}"><a href="" data-page="{{ctx.page}}" class="page-link {{css.paginationButton}}">{{ctx.text}}</a></li>',
      },
    });
    $('#bootgrid-selection').bootgrid({
      selection: true,
      multiSelect: true,
      rowSelect: true,
      keepSelection: true,
      templates: {
        select:
          '<div class="custom-control custom-checkbox">' +
          '<input type="{{ctx.type}}" class="custom-control-input {{css.selectBox}}" id="customCheck1" value="{{ctx.value}}" {{ctx.checked}}>' +
          '<label class="custom-control-label" for="customCheck1"></label>' +
          '</div>',
        // templates for BS4
        actionButton: '<button class="btn btn-secondary" type="button" title="{{ctx.text}}">{{ctx.content}}</button>',
        actionDropDown:
          '<div class="{{css.dropDownMenu}}"><button class="btn btn-secondary dropdown-toggle dropdown-toggle-nocaret" type="button" data-toggle="dropdown"><span class="{{css.dropDownMenuText}}">{{ctx.content}}</span></button><ul class="{{css.dropDownMenuItems}}" role="menu"></ul></div>',
        actionDropDownItem: '<li class="dropdown-item"><a href="" data-action="{{ctx.action}}" class="dropdown-link {{css.dropDownItemButton}}">{{ctx.text}}</a></li>',
        actionDropDownCheckboxItem: '<li class="dropdown-item"><label class="dropdown-item p-0"><input name="{{ctx.name}}" type="checkbox" value="1" class="{{css.dropDownItemCheckbox}}" {{ctx.checked}} /> {{ctx.label}}</label></li>',
        paginationItem: '<li class="page-item {{ctx.css}}"><a href="" data-page="{{ctx.page}}" class="page-link {{css.paginationButton}}">{{ctx.text}}</a></li>',
      },
    });
    var grid = $('#bootgrid-command')
      .bootgrid({
        formatters: {
          commands: function commands(column, row) {
            return (
              '<button type="button" class="btn btn-sm btn-info mr-2 command-edit" data-row-id="' +
              row.id +
              '"><em class="fa fa-edit fa-fw"></em></button>' +
              '<button type="button" class="btn btn-sm btn-danger command-delete" data-row-id="' +
              row.id +
              '"><em class="fa fa-trash fa-fw"></em></button>'
            );
          },
        },
        templates: {
          // templates for BS4
          actionButton: '<button class="btn btn-secondary" type="button" title="{{ctx.text}}">{{ctx.content}}</button>',
          actionDropDown:
            '<div class="{{css.dropDownMenu}}"><button class="btn btn-secondary dropdown-toggle dropdown-toggle-nocaret" type="button" data-toggle="dropdown"><span class="{{css.dropDownMenuText}}">{{ctx.content}}</span></button><ul class="{{css.dropDownMenuItems}}" role="menu"></ul></div>',
          actionDropDownItem: '<li class="dropdown-item"><a href="" data-action="{{ctx.action}}" class="dropdown-link {{css.dropDownItemButton}}">{{ctx.text}}</a></li>',
          actionDropDownCheckboxItem: '<li class="dropdown-item"><label class="dropdown-item p-0"><input name="{{ctx.name}}" type="checkbox" value="1" class="{{css.dropDownItemCheckbox}}" {{ctx.checked}} /> {{ctx.label}}</label></li>',
          paginationItem: '<li class="page-item {{ctx.css}}"><a href="" data-page="{{ctx.page}}" class="page-link {{css.paginationButton}}">{{ctx.text}}</a></li>',
        },
      })
      .on('loaded.rs.jquery.bootgrid', function () {
        /* Executes after data is loaded and rendered */
        grid
          .find('.command-edit')
          .on('click', function () {
            console.log('You pressed edit on row: ' + $(this).data('row-id'));
          })
          .end()
          .find('.command-delete')
          .on('click', function () {
            console.log('You pressed delete on row: ' + $(this).data('row-id'));
          });
      });
  }
})(); // DATATABLES
// -----------------------------------

(function () {
  'use strict';

  $(initDatatables);

  function initDatatables() {
    if (!$.fn.DataTable) return; // Zero configuration

    $('#datatable2').DataTable({
      // retrieve: true,
      paging: true,
      // Table pagination
      ordering: true,
      // Column ordering
      info: true,
      // Bottom left status text
      responsive: true,
      // Text translation options
      // Note the required keywords between underscores (e.g _MENU_)
      oLanguage: {
        sSearch: 'Pesquiza :',
        sLengthMenu: '_MENU_ Dados Kada Pajina',
        sInfo: 'Hamosu Pajina _PAGE_ husi _PAGES_',
        sInfoEmpty: 'Hamosu Pajina _PAGE_ husi _PAGES_',
        sEmptyTable: 'Dados Laiha',
        zeroRecords: 'Dados Laiha - Mamuk(0)',
        infoEmpty: 'Dados Relevante La eziste',
        infoFiltered: '(Filter Dados Husi _MAX_ Total Dados)',
        oPaginate: {
          sNext: '<em class="fa fa-caret-right"></em>',
          sPrevious: '<em class="fa fa-caret-left"></em>',
        },
      },
      // Datatable Buttons setup
      dom: 'Bfrtip',
      buttons: [
        {
          extend: 'excel',
          className: 'btn-info',
          title: 'SIIGSA',
        },
      ],
    });
  }
})();
//new dataTable
(function () {
  'use strict';

  $(initDatatables);

  function initDatatables() {
    if (!$.fn.DataTable) return; // Zero configuration

    $('#datatable1').DataTable({
      retrieve: true,
      paging: true,
      // Table pagination
      ordering: true,
      // Column ordering
      info: true,
      // Bottom left status text
      responsive: true,
      // Text translation options
      // Note the required keywords between underscores (e.g _MENU_)
      oLanguage: {
        sSearch: 'Pesquiza :',
        sLengthMenu: '_MENU_ Dados Kada Pajina',
        sInfo: 'Hamosu Pajina _PAGE_ husi _PAGES_',
        sInfoEmpty: 'Hamosu Pajina _PAGE_ husi _PAGES_',
        sEmptyTable: 'Dados Laiha',
        zeroRecords: 'Dados Laiha - Mamuk(0)',
        infoEmpty: 'Dados Relevante La eziste',
        infoFiltered: '(Filter Dados Husi _MAX_ Total Dados)',
        oPaginate: {
          sNext: '<em class="fa fa-caret-right"></em>',
          sPrevious: '<em class="fa fa-caret-left"></em>',
        },
      },
      // Datatable Buttons setup
      dom: 'Bfrtip',
      buttons: [
        {
          extend: 'copy',
          className: 'btn-info',
        },
        {
          extend: 'csv',
          className: 'btn-info',
        },
        {
          extend: 'excel',
          className: 'btn-info',
          title: 'XLS-File',
        },
        {
          extend: 'pdf',
          className: 'btn-info',
          title: $('title').text(),
        },
        {
          extend: 'print',
          className: 'btn-info',
        },
      ],
    });
  }
})();

/**
 * Used for user pages
 * Login and Register
 */

(function () {
  'use strict';

  $(initParsleyForPages);

  function initParsleyForPages() {
    // Parsley options setup for bootstrap validation classes
    var parsleyOptions = {
      errorClass: 'is-invalid',
      successClass: 'is-valid',
      classHandler: function classHandler(ParsleyField) {
        var el = ParsleyField.$element.parents('.form-group').find('input');
        if (!el.length)
          // support custom checkbox
          el = ParsleyField.$element.parents('.c-checkbox').find('label');
        return el;
      },
      errorsContainer: function errorsContainer(ParsleyField) {
        return ParsleyField.$element.parents('.form-group');
      },
      errorsWrapper: '<div class="text-help">',
      errorTemplate: '<div></div>',
    }; // Login form validation with Parsley

    var loginForm = $('#loginForm');
    if (loginForm.length) loginForm.parsley(parsleyOptions); // Register form validation with Parsley

    var registerForm = $('#registerForm');
    if (registerForm.length) registerForm.parsley(parsleyOptions);
  }
})(); // Custom Code
// -----------------------------------


// utiliza ba minimiza card

(function () {
  'use strict';

  $(initCardDismiss);
  $(initCardCollapse);
  $(initCardRefresh);
  /**
   * Helper function to find the closest
   * ascending .card element
   */

  function getCardParent(item) {
    var el = item.parentElement;

    while (el && !el.classList.contains('card')) {
      el = el.parentElement;
    }

    return el;
  }
  /**
   * Helper to trigger custom event
   */


  function triggerEvent(type, item, data) {
    var ev;

    if (typeof CustomEvent === 'function') {
      ev = new CustomEvent(type, {
        detail: data
      });
    } else {
      ev = document.createEvent('CustomEvent');
      ev.initCustomEvent(type, true, false, data);
    }

    item.dispatchEvent(ev);
  }
  /**
   * Dismiss cards
   * [data-tool="card-dismiss"]
   */


  function initCardDismiss() {
    var cardtoolSelector = '[data-tool="card-dismiss"]';
    var cardList = [].slice.call(document.querySelectorAll(cardtoolSelector));
    cardList.forEach(function (item) {
      new CardDismiss(item);
    });

    function CardDismiss(item) {
      var EVENT_REMOVE = 'card.remove';
      var EVENT_REMOVED = 'card.removed';
      this.item = item;
      this.cardParent = getCardParent(this.item);
      this.removing = false; // prevents double execution

      this.clickHandler = function (e) {
        if (this.removing) return;
        this.removing = true; // pass callbacks via event.detail to confirm/cancel the removal

        triggerEvent(EVENT_REMOVE, this.cardParent, {
          confirm: this.confirm.bind(this),
          cancel: this.cancel.bind(this)
        });
      };

      this.confirm = function () {
        this.animate(this.cardParent, function () {
          triggerEvent(EVENT_REMOVED, this.cardParent);
          this.remove(this.cardParent);
        });
      };

      this.cancel = function () {
        this.removing = false;
      };

      this.animate = function (item, cb) {
        if ('onanimationend' in window) {
          // animation supported
          item.addEventListener('animationend', cb.bind(this));
          item.className += ' animated bounceOut'; // requires animate.css
        } else cb.call(this); // no animation, just remove

      };

      this.remove = function (item) {
        item.parentNode.removeChild(item);
      }; // attach listener


      item.addEventListener('click', this.clickHandler.bind(this), false);
    }
  }
  /**
   * Collapsed cards
   * [data-tool="card-collapse"]
   * [data-start-collapsed]
   */


  function initCardCollapse() {
    var cardtoolSelector = '[data-tool="card-collapse"]';
    var cardList = [].slice.call(document.querySelectorAll(cardtoolSelector));
    cardList.forEach(function (item) {
      var initialState = item.hasAttribute('data-start-collapsed');
      new CardCollapse(item, initialState);
    });

    function CardCollapse(item, startCollapsed) {
      var EVENT_SHOW = 'card.collapse.show';
      var EVENT_HIDE = 'card.collapse.hide';
      this.state = true; // true -> show / false -> hide

      this.item = item;
      this.cardParent = getCardParent(this.item);
      this.wrapper = this.cardParent.querySelector('.card-wrapper');

      this.toggleCollapse = function (action) {
        triggerEvent(action ? EVENT_SHOW : EVENT_HIDE, this.cardParent);
        this.wrapper.style.maxHeight = (action ? this.wrapper.scrollHeight : 0) + 'px';
        this.state = action;
        this.updateIcon(action);
      };

      this.updateIcon = function (action) {
        this.item.firstElementChild.className = action ? 'fa fa-minus' : 'fa fa-plus';
      };

      this.clickHandler = function () {
        this.toggleCollapse(!this.state);
      };

      this.initStyles = function () {
        this.wrapper.style.maxHeight = this.wrapper.scrollHeight + 'px';
        this.wrapper.style.transition = 'max-height 0.5s';
        this.wrapper.style.overflow = 'hidden';
      }; // prepare styles for collapse animation


      this.initStyles(); // set initial state if provided

      if (startCollapsed) {
        this.toggleCollapse(false);
      } // attach listener


      this.item.addEventListener('click', this.clickHandler.bind(this), false);
    }
  }
  /**
   * Refresh cards
   * [data-tool="card-refresh"]
   * [data-spinner="standard"]
   */


  function initCardRefresh() {
    var cardtoolSelector = '[data-tool="card-refresh"]';
    var cardList = [].slice.call(document.querySelectorAll(cardtoolSelector));
    cardList.forEach(function (item) {
      new CardRefresh(item);
    });

    function CardRefresh(item) {
      var EVENT_REFRESH = 'card.refresh';
      var WHIRL_CLASS = 'whirl';
      var DEFAULT_SPINNER = 'standard';
      this.item = item;
      this.cardParent = getCardParent(this.item);
      this.spinner = ((this.item.dataset || {}).spinner || DEFAULT_SPINNER).split(' '); // support space separated classes

      this.refresh = function (e) {
        var card = this.cardParent; // start showing the spinner

        this.showSpinner(card, this.spinner); // attach as public method

        card.removeSpinner = this.removeSpinner.bind(this); // Trigger the event and send the card

        triggerEvent(EVENT_REFRESH, card, {
          card: card
        });
      };

      this.showSpinner = function (card, spinner) {
        card.classList.add(WHIRL_CLASS);
        spinner.forEach(function (s) {
          card.classList.add(s);
        });
      };

      this.removeSpinner = function () {
        this.cardParent.classList.remove(WHIRL_CLASS);
      }; // attach listener


      this.item.addEventListener('click', this.refresh.bind(this), false);
    }
  }
})(); // GLOBAL CONSTANTS
// -----------------------------------










// select2===========================
(function () {
  'use strict';

  $(initSelect2);

  function initSelect2() {
    if (!$.fn.select2) return; // Select 2

    $('#select2-1').select2({
      theme: 'bootstrap4'
    });
    $('#select2-2').select2({
      theme: 'bootstrap4'
    });
    $('#select2-3').select2({
      theme: 'bootstrap4'
    });
    $('#select2-4').select2({
      placeholder: 'Select a state',
      allowClear: true,
      theme: 'bootstrap4'
    });
  }
})();

// select2===========================




















/**
 * Refresh cards
 * [data-tool="card-refresh"]
 * [data-spinner="standard"]
 */




(function () {
  'use strict';

  $(initCustom);

  function initCustom() {
    // custom code
  }
})();
