import ConversionItem from './Conversion'

export default function ConversionView(props) {
    return (
        <div>
            <ul>
                {props.todoList.map(todo => <ConversionItem todo={todo} />)}
            </ul>
        </div>
    )
}