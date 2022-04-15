import React from 'react';

import { Table as BsTable, Button } from 'react-bootstrap';
import { get } from 'lodash'

import style from './table.module.scss';

const Table = ({ columns, data, actions }) => {
  return (
    <BsTable>
      <thead>
        <tr>
          {columns.map(([columnName, columnKey]) => <th key={columnKey}>{columnName}</th>)}
          {actions && <th>Actions</th>}
        </tr>
      </thead>
      <tbody>
        {data.map((row, i) => 
          <tr key={i}>
            {columns.map(([_, columnKey]) => 
              <td key={`${i}-${columnKey}`}>{get(row, columnKey, '')}</td>)}
           {actions && <td className={style.actions}>
              {(actions || []).map(([actionName, actionCallback]) => 
                <Button 
                  variant='outline-primary' 
                  key={`${i}-${actionName}`} 
                  onClick={() => actionCallback(i)}
                >
                  {actionName}
                </Button>)}
            </td>}
          </tr>)}
      </tbody>
    </BsTable>
  )
}

export default Table;
