import React from "react";
import "./css/MyReusableTable.module.css"; 

interface TableProps<T extends Record<string, any>> {
  data: T[];
  columns: {
    key: keyof T;
    header: string;
    render?: (item: T) => React.ReactNode;
  }[];
}

const Table = <T extends Record<string, any>>({ data, columns }: TableProps<T>) => {
  if (!data || data.length === 0) {
    return <p>No data to display.</p>;
  }
  if (!columns || columns.length === 0) {
    return <p>No columns defined.</p>;
  }
  return (
    <table className="data-table">
      <thead>
        <tr>
          {columns.map((column) => (
            <th key={column.key.toString()}>{column.header}</th>
          ))}
        </tr>
      </thead>
      <tbody>
        {data.map((item, index) => (
          <tr key={index}>
            {columns.map((column) => (
              <td key={`${index}-${column.key.toString()}`}>
                {column.render ? column.render(item) : item[column.key]}
              </td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  );
};

export default Table;