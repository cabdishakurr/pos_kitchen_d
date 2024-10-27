/** @odoo-module **/

import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { Component, useState, onWillStart } from "@odoo/owl";

class KitchenD extends Component {
    setup() {
        this.orm = useService("orm");
        this.state = useState({
            orders: [],
            filter: 'all'
        });

        onWillStart(async () => {
            await this.fetchOrders();
        });
    }

    async fetchOrders() {
        this.state.orders = await this.orm.searchRead('pos.kitchen.d.order', [], [
            'name', 'table_id', 'customer_name', 'state', 'order_line_ids', 'order_time'
        ]);
    }

    get filteredOrders() {
        return this.state.orders.filter(order => 
            this.state.filter === 'all' || order.state === this.state.filter
        );
    }

    get orderCounts() {
        return {
            to_cook: this.state.orders.filter(o => o.state === 'to_cook').length,
            ready: this.state.orders.filter(o => o.state === 'ready').length,
            completed: this.state.orders.filter(o => o.state === 'completed').length,
        };
    }

    async updateOrderState(orderId, newState) {
        await this.orm.write('pos.kitchen.d.order', [orderId], { state: newState });
        await this.fetchOrders();
    }

    setFilter(filter) {
        this.state.filter = filter;
    }
}

KitchenD.template = 'pos_kitchen_d.KitchenD';

registry.category("views").add("kitchen_d", KitchenD);

export default KitchenD;
