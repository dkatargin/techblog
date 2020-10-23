import React from "react";

export default class CalendarBlock extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            loading: true,
        };

        this.handleData = this.handleData.bind(this);
    }

}