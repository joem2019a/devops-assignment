import React, { useMemo } from 'react';
import { useHistory, useLocation, Link } from 'react-router-dom';

import { GoChevronLeft } from 'react-icons/go';
import { Button, Breadcrumb } from 'react-bootstrap';
import { kebabCase, startCase, slice } from 'lodash';

import style from './page-header.module.scss';

const PageHeader = ({ onBack }) => {
  const history = useHistory();
  const location = useLocation();
  const back = history.goBack;

  const pathParts = useMemo(
    () => location.pathname.split('/'),
    [location.pathname]
  );

  return (
    <div className={style.pageHeader}>
      <Button
        variant="outline-primary"
        onClick={onBack ?? back}
        title="Go Back"
        className={style.backButton}
      >
        <GoChevronLeft /> Back
      </Button>
      <Breadcrumb>
        {pathParts.map((pathPart, index) => (
          <Breadcrumb.Item
            key={pathPart}
            linkAs={Link}
            linkProps={{ to: slice(pathParts, 0, index + 1).join('/') || '/' }}
            active={index === pathParts.length - 1}
          >
            {startCase(kebabCase(pathPart || 'Home'))}
          </Breadcrumb.Item>
        ))}
      </Breadcrumb>
    </div>
  );
};

export default PageHeader;
