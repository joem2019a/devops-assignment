import React from 'react';

import { Table as BsTable } from 'react-bootstrap';
import { get } from 'lodash'

const Table = ({ columns, data }) => {
  return (
    <BsTable>
      <thead>
        <tr>
          {columns.map(([columnName, columnKey]) => <th key={columnKey}>{columnName}</th>)}
        </tr>
      </thead>
      <tbody>
        {data.map((row, i) => 
          <tr key={i}>
            {columns.map(([_, columnKey]) => 
              <td key={`${i}-${columnKey}`}>{get(row, columnKey, '')}</td>)}
          </tr>)}
      </tbody>
    </BsTable>
  )
}

export default Table;
