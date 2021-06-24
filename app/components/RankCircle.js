import React from 'react';
import './RankCircle.css';
import {
    first_arc_border_color, 
    second_arc_border_color,
    second_arc_transform
} from './colorFunctions';


const RankCircle = ({ rank }) => {
    // Style for first arc
    const firstArcStyle = {
        borderColor: first_arc_border_color(rank),
    };
    // Style for second arc
    const secondArcStyle = {
        borderColor: second_arc_border_color(rank),
        transform: "rotate(" + second_arc_transform(rank) + "deg)",
    };

    return (
        <div>
            <div className="circle">
                <div className="rank-text">{rank}</div>
            </div>
            <div className="arc" style={firstArcStyle}></div>
            <div className="arc" style={secondArcStyle}></div>
        </div>
    );
}

export default RankCircle;