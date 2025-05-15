/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

class MyCustomView extends Component {
  static template = "regionalizacion.my_custom_view_action";

  setup() {
    this.action = useService("action");
  }
}

// Creamos la función de acción de cliente adecuada
export const myCustomViewAction = {
  component: MyCustomView,
};

// Registramos la acción del cliente correctamente
registry
  .category("actions")
  .add("regionalizacion.my_custom_view_action", MyCustomView);

export default MyCustomView;
