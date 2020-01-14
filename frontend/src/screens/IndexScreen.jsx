import React from "react";
import {Link} from "react-router-dom";
import Fetcher from "../utils";
import '../App.css'

export default class IndexScreen extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            loading: true,
        };

        this.handleData = this.handleData.bind(this);
        this.entityCards = this.entityCards.bind(this);
    }

    handleData(data) {
        this.setState({loading: false, data: data})
    }

    componentDidMount() {
        Fetcher('/api/entities/', 'GET', this.handleData)
    }

    formatDateTime(timeString) {
        let dateObj = new Date(timeString);
        return `${("0" + dateObj.getDay()).slice(-2)}/${("0" + (dateObj.getMonth() + 1)).slice(-2)}/${dateObj.getFullYear()} ${dateObj.getHours()}:${dateObj.getMinutes()}`
    }

    entityCards() {
        let cards = [];
        for (let i = 0; i < this.state.data.length; i++) {
            const item = this.state.data[i];
            let dates = <div className="card-creation_date">{this.formatDateTime(item.creation_date)}</div>;
            if (this.formatDateTime(item.edit_date) !== this.formatDateTime(item.creation_date)) {
                dates = <React.Fragment>
                    <div key={'cdate__' + item.slug}
                         className="card-creation_date">{this.formatDateTime(item.creation_date)}</div>

                    <div key={'update__' + item.slug}
                         className="card-edit_date">(updated at: {this.formatDateTime(item.edit_date)})
                    </div>

                </React.Fragment>
            }
            cards.push(<div key={item.slug} className="content-card content-background">
                <div key={'card_title__' + item.slug} className="card-title"><Link to={`/${item.slug}/`}>{item.title}</Link></div>
                <div key={'card_prev__' + item.slug} className="card-preview">{item.preview}</div>
                <div key={'card_footer__' + item.slug} className="card-footer">
                    {dates}
                </div>
            </div>)
        }
        return cards
    }

    render() {
        if (this.state.loading) {
            return null
        }
        return (
            <div>{this.entityCards()}</div>
        )
    }

}
