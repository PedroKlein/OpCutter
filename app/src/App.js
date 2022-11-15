import React, { Component } from 'react'
import ReactPlayer from 'react-player'

const url_ = URL.revokeObjectURL('D:/Series-filmes/Westworld S2/Westworld.S02E07.MP4.LEG.BaixarSeriesMP4.Com.mp4')

export default class App extends Component {
    render() {
        return <ReactPlayer url = { url_ }
        playing / >
    }
}